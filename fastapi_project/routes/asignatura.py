from fastapi import APIRouter, HTTPException, status
from service.asignatura import AsignaturaDB
from shemas.asignaturaShema import AsignaturaRegister, AsignaturaUpdate, AsignaturaResponse
from typing import List

router = APIRouter()

"""
    Rutas para la tabla ASIGNATURA
"""
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=AsignaturaResponse)
async def create_asignatura(asignatura: AsignaturaRegister):
    try:
        return AsignaturaDB.insert_asignatura(asignatura)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al registrar asignatura"
        )

"""
    Rutas para la tabla ASIGNATURA
"""
@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[AsignaturaResponse])
async def get_all_asignaturas():
    try:
        return AsignaturaDB.get_all_asignaturas()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener asignaturas"
        )

"""
    Rutas para la tabla ASIGNATURA
"""
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AsignaturaResponse)
async def get_asignatura_by_id(id: int):
    try:
        return AsignaturaDB.get_asignatura_by_id(id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener asignatura"
        )

"""
    Rutas para la tabla ASIGNATURA
"""
@router.put("/update/{id}", status_code=status.HTTP_200_OK, response_model=AsignaturaResponse)
async def update_asignatura(id: int, asignatura: AsignaturaUpdate):
    try:
        return AsignaturaDB.update_asignatura(id, asignatura)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al actualizar asignatura"
        )


"""
    Rutas para la tabla ASIGNATURA
"""
@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_asignatura(id: int):
    try:
        return AsignaturaDB.delete_asignatura(id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al eliminar asignatura"
        )
