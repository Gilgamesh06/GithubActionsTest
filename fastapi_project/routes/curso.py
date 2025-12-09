from fastapi import APIRouter, HTTPException, status
from service.curso import CursoDB
from shemas.cursoShema import CursoRegister, CursoUpdate, CursoResponse
from typing import List

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=CursoResponse)
async def create_curso(curso: CursoRegister):
    try:
        result = CursoDB.insert_curso(curso)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al registrar curso"
        )


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[CursoResponse])
async def get_all_cursos():
    try:
        result = CursoDB.get_all_cursos()
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener cursos"
        )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CursoResponse)
async def get_curso_by_id(id: int):
    try:
        result = CursoDB.get_curso_by_id(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al obtener curso"
        )


@router.put("/update/{id}", status_code=status.HTTP_200_OK, response_model=CursoResponse)
async def update_curso(id: int, curso: CursoUpdate):
    try:
        result = CursoDB.update_curso(id, curso)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al actualizar curso"
        )


@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_curso(id: int):
    try:
        result = CursoDB.delete_curso(id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error inesperado al eliminar curso"
        )
