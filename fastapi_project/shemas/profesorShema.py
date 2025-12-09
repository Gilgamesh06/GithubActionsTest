from pydantic import BaseModel, Field, field_validator, ConfigDict
from shemas.genero import GeneroEnum

# Registro de un profesor
class ProfesorRegister(BaseModel):
    NOMBRE: str = Field(..., min_length=3, max_length=50)
    APELLIDO: str = Field(..., min_length=3, max_length=50)
    EDAD: int = Field(..., ge=18)
    GENERO: GeneroEnum = Field(..., min_length=1, max_length=1)
    
    
    @field_validator('NOMBRE', 'APELLIDO')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()

# Actualizacion de un profesor
class ProfesorUpdate(BaseModel):
    NOMBRE: str = Field(..., min_length=3, max_length=50)
    APELLIDO: str = Field(..., min_length=3, max_length=50)
    EDAD: int = Field(..., ge=18)
    GENERO: GeneroEnum = Field(..., min_length=1, max_length=1)
        
    @field_validator('NOMBRE', 'APELLIDO')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()


# Response de un profesor
class ProfesorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    ID_PROFESOR: int
    NOMBRE: str
    APELLIDO: str
    EDAD: int
    GENERO: str