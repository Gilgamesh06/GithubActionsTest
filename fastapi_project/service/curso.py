from config.db import DatabaseConnection
from shemas.cursoShema import CursoRegister, CursoUpdate, CursoResponse
from psycopg2.extras import RealDictCursor
from typing import List


class CursoDB:
    
    @staticmethod
    def insert_curso(curso: CursoRegister) -> CursoResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO \"CURSO\" (\"NOMBRE\", \"FID_ASIGNATURA\", \"FID_PROFESOR\") VALUES (%s, %s, %s) RETURNING *",
                    (curso.NOMBRE, curso.FID_ASIGNATURA, curso.FID_PROFESOR)
                )
                conn.commit()
                row = cursor.fetchone()
                return CursoResponse(**row)


    @staticmethod
    def get_all_cursos() -> List[CursoResponse]:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"CURSO\"")
                rows = cursor.fetchall()
                cursos = [CursoResponse(**row) for row in rows]
                return cursos

    @staticmethod
    def get_curso_by_id(id: int) -> CursoResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"CURSO\" WHERE \"ID_CURSO\" = %s", (id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Curso con ID {id} no encontrado")
                return CursoResponse(**row)


    @staticmethod
    def update_curso(id: int, curso: CursoUpdate) -> CursoResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "UPDATE \"CURSO\" SET \"NOMBRE\" = %s, \"FID_ASIGNATURA\" = %s, \"FID_PROFESOR\" = %s WHERE \"ID_CURSO\" = %s RETURNING *",
                    (curso.NOMBRE, curso.FID_ASIGNATURA, curso.FID_PROFESOR, id)
                )
                conn.commit()
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Curso con ID {id} no encontrado")
                return CursoResponse(**row)

    
    @staticmethod
    def delete_curso(id: int) -> dict:
        with DatabaseConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM \"CURSO\" WHERE \"ID_CURSO\" = %s", (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    raise ValueError(f"Curso con ID {id} no encontrado")
                return {"message": "Curso eliminado exitosamente", "id": id}
