import os
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from urllib.parse import urlparse

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos
DATABASE_URL = os.getenv('DATABASE_URL')

# Parsear la URL de la base de datos
url = urlparse(DATABASE_URL)

# Configuración de la base de datos
DB_CONFIG = {
    'host': url.hostname,
    'port': url.port or 5432,
    'database': url.path[1:],  # Remover el '/' inicial
    'user': url.username,
    'password': url.password
}

# Pool de conexiones (opcional pero recomendado para producción)
connection_pool = None

def init_connection_pool(minconn=1, maxconn=10):
    """
    Inicializa el pool de conexiones a la base de datos.
    
    Args:
        minconn: Número mínimo de conexiones en el pool
        maxconn: Número máximo de conexiones en el pool
    """
    global connection_pool
    try:
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn,
            maxconn,
            **DB_CONFIG
        )
        if connection_pool:
            print("✓ Pool de conexiones creado exitosamente")
    except (Exception, psycopg2.Error) as error:
        print(f"✗ Error al crear el pool de conexiones: {error}")
        raise

def get_connection():
    """
    Obtiene una conexión del pool o crea una nueva conexión.
    
    Returns:
        Conexión a la base de datos
    """
    if connection_pool:
        return connection_pool.getconn()
    else:
        return psycopg2.connect(**DB_CONFIG)

def release_connection(conn):
    """
    Libera una conexión de vuelta al pool.
    
    Args:
        conn: Conexión a liberar
    """
    if connection_pool:
        connection_pool.putconn(conn)
    else:
        conn.close()

def close_all_connections():
    """
    Cierra todas las conexiones del pool.
    """
    global connection_pool
    if connection_pool:
        connection_pool.closeall()
        print("✓ Todas las conexiones cerradas")

class DatabaseConnection:
    """
    Context manager para manejar conexiones de base de datos de forma segura.
    
    Uso:
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tabla")
            results = cursor.fetchall()
    """
    def __init__(self, cursor_factory=None):
        """
        Args:
            cursor_factory: Factory para el cursor (ej: RealDictCursor para obtener resultados como diccionarios)
        """
        self.conn = None
        self.cursor_factory = cursor_factory
    
    def __enter__(self):
        self.conn = get_connection()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Si hubo un error, hacer rollback
            self.conn.rollback()
        else:
            # Si todo salió bien, hacer commit
            self.conn.commit()
        
        release_connection(self.conn)
        return False

def execute_query(query, params=None, fetch=True, dict_cursor=False):
    """
    Ejecuta una consulta SQL y retorna los resultados.
    
    Args:
        query: Consulta SQL a ejecutar
        params: Parámetros para la consulta (opcional)
        fetch: Si True, retorna los resultados. Si False, solo ejecuta la consulta
        dict_cursor: Si True, retorna resultados como diccionarios
    
    Returns:
        Resultados de la consulta o None
    """
    cursor_factory = RealDictCursor if dict_cursor else None
    
    with DatabaseConnection() as conn:
        cursor = conn.cursor(cursor_factory=cursor_factory)
        cursor.execute(query, params)
        
        if fetch:
            return cursor.fetchall()
        else:
            return cursor.rowcount

