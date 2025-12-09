from fastapi import APIRouter, HTTPException, status
from service.matricula import MatriculaDB
from shemas.matriculaShema import MatriculaRegister, MatriculaUpdate, MatriculaResponse
from typing import List

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=MatriculaResponse)
async def create_matricula(matricula: MatriculaRegister):
    try:
        result = MatriculaDB.insert_matricula(matricula)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al registrar matricula"
        )

@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[MatriculaResponse])
async def get_all_matriculas():
    try:
        result = MatriculaDB.get_all_matriculas()
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener matriculas"
        )

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=MatriculaResponse)
async def get_matricula_by_id(id: int):
    try:
        result = MatriculaDB.get_matricula_by_id(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener matricula"
        )

@router.put("/update/{id}", status_code=status.HTTP_200_OK, response_model=MatriculaResponse)
async def update_matricula(id: int, matricula: MatriculaUpdate):
    try:
        result = MatriculaDB.update_matricula(id, matricula)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al actualizar matricula"
        )

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_matricula(id: int):
    try:
        result = MatriculaDB.delete_matricula(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al eliminar matricula"
        )

