from pydantic import BaseModel, Field, ConfigDict

# Registro de un curso
class CursoRegister(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100)
    FID_ASIGNATURA: int = Field(..., ge=1)
    FID_PROFESOR: int = Field(..., ge=1)

# Actualizacion de un curso
class CursoUpdate(BaseModel):
    NOMBRE: str = Field(..., min_length=1, max_length=100)
    FID_ASIGNATURA: int = Field(..., ge=1)
    FID_PROFESOR: int = Field(..., ge=1)

# Response de un curso
class CursoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    ID_CURSO: int
    NOMBRE: str
    FID_ASIGNATURA: int
    FID_PROFESOR: int
