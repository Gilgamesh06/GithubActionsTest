from pydantic import BaseModel, Field, field_validator, ConfigDict

# Registro de una asignatura
class AsignaturaRegister(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100, description="Nombre de la asignatura")
    CREDITOS: int = Field(..., ge=1, le=10, description="Creditos de la asignatura")
    
    @field_validator('NOMBRE')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()

# Actualizacion de una asignatura
class AsignaturaUpdate(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100, description="Nombre de la asignatura")
    CREDITOS: int = Field(..., ge=1, le=10, description="Creditos de la asignatura")
    
    @field_validator('NOMBRE')
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("El campo no puede estar vacío")
        return v.strip()

# Response de una asignatura
class AsignaturaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    ID_ASIGNATURA: int
    NOMBRE: str
    CREDITOS: int

