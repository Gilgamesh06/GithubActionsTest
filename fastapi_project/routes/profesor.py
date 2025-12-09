from fastapi import APIRouter
from shemas.profesorShema import ProfesorRegister, ProfesorUpdate, ProfesorResponse
from service.profesor import ProfesorDB
from typing import List
from fastapi import HTTPException, status

router = APIRouter()

"""
    Registro de un profesor
"""
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=ProfesorResponse)
async def register_profesor(profesor: ProfesorRegister):
    return ProfesorDB.insert_profesor(profesor)

"""
    Obtenemos todos los profesores
"""
@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[ProfesorResponse])
async def get_all_profesores():
    return ProfesorDB.get_all_profesores()

"""
    Obtenemos un profesor por su id
"""
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProfesorResponse)
async def get_profesor_by_id(id: int):
    try:
        result = ProfesorDB.get_profesor_by_id(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener profesor"
        )

"""
    Actualizamos un profesor por su id
"""
@router.put("/update/{id}", status_code=status.HTTP_200_OK, response_model=ProfesorResponse)
async def update_profesor(id: int, profesor: ProfesorUpdate):
    try:
        result = ProfesorDB.update_profesor(id, profesor)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al actualizar profesor"
        )

"""
    Eliminamos un profesor por su id
"""
@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_profesor(id: int):
    try:
        result = ProfesorDB.delete_profesor(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al eliminar profesor"
        )