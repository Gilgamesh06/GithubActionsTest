import pytest
import sys
import os
import time
import psycopg2
from pathlib import Path
from testcontainers.postgres import PostgresContainer

# Add project root to python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from config import db as app_db
from main import app
from fastapi.testclient import TestClient

SQL_DIR = project_root.parent / "Data_base"

@pytest.fixture(scope="session")
def postgres_container():
    """
    Fixture que inicia un contenedor de PostgreSQL para pruebas de integración.
    Define los parámetros del contenedor: DB_NAME, USER_NAME, USER_PASSWORD, PORT.
    """
    # Parámetros del contenedor
    db_name = "test_db"
    user_name = "test_user"
    user_password = "test_password"
    
    # Iniciar contenedor
    postgres = PostgresContainer("postgres:15", 
                                 dbname=db_name, 
                                 username=user_name, 
                                 password=user_password)
    postgres.start()
    
    # Obtener configuración de conexión del contenedor
    # Testcontainers mapea el puerto 5432 a un puerto aleatorio
    mapped_port = postgres.get_exposed_port(5432)
    host = postgres.get_container_host_ip()
    
    # Crear nueva configuración para la app
    new_db_config = {
        'host': host,
        'port': mapped_port,
        'database': db_name,
        'user': user_name,
        'password': user_password
    }
    
    # Actualizar la configuración en la aplicación
    app_db.DB_CONFIG = new_db_config
    
    # Inicializar el pool de conexiones con la nueva configuración
    app_db.init_connection_pool(minconn=1, maxconn=5)
    
    # Ejecutar scripts SQL (db.sql y insert.sql)
    conn = psycopg2.connect(**new_db_config)
    try:
        with conn.cursor() as cursor:
            # Crear tablas
            db_script_path = SQL_DIR / "db.sql"
            if db_script_path.exists():
                with open(db_script_path, "r") as f:
                    cursor.execute(f.read())
            else:
                print(f"Warning: {db_script_path} not found")

            # Insertar datos
            insert_script_path = SQL_DIR / "insert.sql"
            if insert_script_path.exists():
                with open(insert_script_path, "r") as f:
                    cursor.execute(f.read())
            else:
                print(f"Warning: {insert_script_path} not found")
                
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        conn.close()
        
    yield postgres
    
    # Cleanup
    app_db.close_all_connections()
    postgres.stop()

@pytest.fixture
def client(postgres_container):
    """
    Fixture que proporciona un cliente de prueba para la aplicación FastAPI.
    Depende de postgres_container para asegurar que la BD esté lista.
    """
    return TestClient(app)



@pytest.fixture
def estudiante_data():
    """
    Fixture con datos válidos de estudiante para tests
    """
    return {
        "NOMBRE": "Juan",
        "APELLIDO": "Pérez",
        "EDAD": 20,
        "GENERO": "M"
    }

@pytest.fixture
def asignatura_data():
    """
    Fixture con datos válidos de asignatura para tests
    """
    return {
        "NOMBRE": "Matemáticas Avanzadas",
        "CREDITOS": 5
    }

@pytest.fixture
def profesor_data():
    """
    Fixture con datos válidos de profesor para tests
    """
    return {
        "NOMBRE": "Albert",
        "APELLIDO": "Einstein",
        "EDAD": 55,
        "GENERO": "M"
    }

@pytest.fixture
def curso_data():
    """
    Fixture con datos válidos de curso para tests
    """
    return {
        "NOMBRE": "Física Cuántica",
        "FID_ASIGNATURA": 1,
        "FID_PROFESOR": 1
    }

@pytest.fixture
def matricula_data():
    """
    Fixture con datos válidos de matrícula para tests
    """
    return {
        "FID_ESTUDIANTE": 1,
        "FID_CURSO": 1
    }
