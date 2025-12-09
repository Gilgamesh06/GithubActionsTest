from pydantic import BaseModel, Field, ConfigDict

# Registro de una matricula
class MatriculaRegister(BaseModel):
    FID_ESTUDIANTE: int = Field(..., ge=1)
    FID_CURSO: int = Field(..., ge=1)

# Actualizacion de una matricula
class MatriculaUpdate(BaseModel):
    FID_ESTUDIANTE: int = Field(..., ge=1)
    FID_CURSO: int = Field(..., ge=1)

# Response de una matricula
class MatriculaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    ID_MATRICULA: int
    FID_ESTUDIANTE: int
    FID_CURSO: int