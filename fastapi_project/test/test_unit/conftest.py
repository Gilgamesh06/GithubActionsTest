"""
Configuración de fixtures compartidos para todos los tests unitarios
"""
import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch

# Add project root to python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from fastapi.testclient import TestClient
from main import app 

@pytest.fixture
def client():
    """
    Fixture que proporciona un cliente de prueba para la aplicación FastAPI
    """
    return TestClient(app)

@pytest.fixture
def mock_db_connection():
    """
    Mock de la conexión a la base de datos
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    return mock_conn, mock_cursor

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
def estudiante_response():
    """
    Fixture con respuesta esperada de estudiante
    """
    return {
        "ID_ESTUDIANTE": 1,
        "NOMBRE": "Juan",
        "APELLIDO": "Pérez",
        "EDAD": 20,
        "GENERO": "M"
    }

@pytest.fixture
def profesor_data():
    """
    Fixture con datos válidos de profesor para tests
    """
    return {
        "NOMBRE": "María",
        "APELLIDO": "González",
        "EDAD": 35,
        "GENERO": "F"
    }

@pytest.fixture
def profesor_response():
    """
    Fixture con respuesta esperada de profesor
    """
    return {
        "ID_PROFESOR": 1,
        "NOMBRE": "María",
        "APELLIDO": "González",
        "EDAD": 35,
        "GENERO": "F"
    }

@pytest.fixture
def asignatura_data():
    """
    Fixture con datos válidos de asignatura para tests
    """
    return {
        "NOMBRE": "Matemáticas",
        "CREDITOS": 5
    }

@pytest.fixture
def asignatura_response():
    """
    Fixture con respuesta esperada de asignatura
    """
    return {
        "ID_ASIGNATURA": 1,
        "NOMBRE": "Matemáticas",
        "CREDITOS": 5
    }

@pytest.fixture
def curso_data():
    """
    Fixture con datos válidos de curso para tests
    """
    return {
        "NOMBRE": "Cálculo I",
        "FID_ASIGNATURA": 1,
        "FID_PROFESOR": 1
    }

@pytest.fixture
def curso_response():
    """
    Fixture con respuesta esperada de curso
    """
    return {
        "ID_CURSO": 1,
        "NOMBRE": "Cálculo I",
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

@pytest.fixture
def matricula_response():
    """
    Fixture con respuesta esperada de matrícula
    """
    return {
        "ID_MATRICULA": 1,
        "FID_ESTUDIANTE": 1,
        "FID_CURSO": 1
    }
