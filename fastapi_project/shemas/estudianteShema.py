from pydantic import BaseModel, Field, field_validator, ConfigDict
from shemas.genero import GeneroEnum

# Registro de un estudiante
class EstudianteRegister(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100, description="Nombre del estudiante")
    APELLIDO: str = Field(..., min_length=1, max_length=100, description="Apellido del estudiante")
    EDAD: int = Field(..., ge=5, le=100, description="Edad del estudiante (entre 5 y 100 años)")
    GENERO: GeneroEnum = Field(..., description="Género del estudiante (M, F, O)")
    
    @field_validator('NOMBRE', 'APELLIDO')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()

# Actualizacion de un estudiante
class EstudianteUpdate(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100, description="Nombre del estudiante")
    APELLIDO: str = Field(..., min_length=1, max_length=100, description="Apellido del estudiante")
    EDAD: int = Field(..., ge=5, le=100, description="Edad del estudiante (entre 5 y 100 años)")
    GENERO: GeneroEnum = Field(..., description="Género del estudiante (M, F, O)")
    
    @field_validator('NOMBRE', 'APELLIDO')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()

# Response de un estudiante
class EstudianteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    ID_ESTUDIANTE: int
    NOMBRE: str
    APELLIDO: str
    EDAD: int
    GENERO: str
