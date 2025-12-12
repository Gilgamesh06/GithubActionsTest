from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.db import init_connection_pool, close_all_connections, execute_query
from routes.estudiante import router as router_estudiantes
from routes.asignatura import router as router_asignaturas
from routes.profesor import router as router_profesores
from routes.curso import router as router_cursos
from routes.matricula import router as router_matriculas


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager para manejar el ciclo de vida de la aplicación.
    Código antes del yield se ejecuta al iniciar.
    Código después del yield se ejecuta al cerrar.
    """
    # STARTUP: Inicializar el pool de conexiones
    print("🚀 Iniciando aplicación...")
    init_connection_pool(minconn=2, maxconn=10)
    print("✅ Aplicación iniciada correctamente")
    
    yield  # La aplicación está corriendo
    
    # SHUTDOWN: Cerrar todas las conexiones
    print("🛑 Cerrando aplicación...")
    close_all_connections()
    print("✅ Aplicación cerrada correctamente")


app = FastAPI(lifespan=lifespan)

# Configuración de CORS
origins = [
    "http://20.94.44.65:8000/" # server test
    "http://localhost:8000",  # Django development server
    "http://127.0.0.1:8000",  # Django development server (alternative)
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True,  # Permitir cookies y credenciales
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

app.include_router(router_estudiantes, prefix="/estudiantes", tags=["estudiantes"])
app.include_router(router_asignaturas, prefix="/asignaturas", tags=["asignaturas"])
app.include_router(router_profesores, prefix="/profesores", tags=["profesores"])
app.include_router(router_cursos, prefix="/cursos", tags=["cursos"])
app.include_router(router_matriculas, prefix="/matriculas", tags=["matriculas"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
