from shemas.estudianteShema import EstudianteRegister, EstudianteUpdate, EstudianteResponse
from fastapi import APIRouter, HTTPException, status
from service.estudiante import EstudianteDB
from typing import List
import psycopg2
import traceback

router = APIRouter()

"""
    Registro de un estudiante
"""
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=EstudianteResponse)
async def insert_estudiante(estudiante: EstudianteRegister):
    try:
        result = EstudianteDB.insert_estudiante(estudiante)
        return result
    except psycopg2.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Error de integridad: El estudiante ya existe o viola restricciones de la base de datos"
        )
    except psycopg2.Error as e:
        # Captura la traza de error
        error_trace = traceback.format_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error de base de datos al registrar estudiante {str(e)}\nTraza de error: {error_trace}"
        )
    except Exception as e:
        # Captura la traza de error
        error_trace = traceback.format_exc()
        # Lanza la excepción HTTP con la traza
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error inesperado al registrar estudiante: {str(e)}\nTraza de error: {error_trace}"
        )

"""
    Obtenemos todos los estudiantes
"""
@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[EstudianteResponse])
async def get_all_estudiantes():
    try:
        result = EstudianteDB.get_all_estudiantes()
        return result
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error de base de datos al obtener estudiantes"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener estudiantes"
        )


"""
    Obtenemos un estudiante por su id
"""
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EstudianteResponse)
async def get_estudiante_by_id(id: int):
    try:
        result = EstudianteDB.get_estudiante_by_id(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error de base de datos al obtener estudiante"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener estudiante"
        )


"""
    Actualizamos un estudiante por su id
"""
@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=EstudianteResponse)
async def update_estudiante(id: int, estudiante: EstudianteUpdate):
    try:
        result = EstudianteDB.update_estudiante(id, estudiante)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except psycopg2.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Error de integridad al actualizar estudiante"
        )
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error de base de datos al actualizar estudiante"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al actualizar estudiante"
        )


"""
    Eliminamos un estudiante por su id
"""
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_estudiante(id: int):
    try:
        result = EstudianteDB.delete_estudiante(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except psycopg2.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="No se puede eliminar: el estudiante tiene registros relacionados"
        )
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error de base de datos al eliminar estudiante"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al eliminar estudiante"
        )
