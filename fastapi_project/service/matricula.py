from config.db import DatabaseConnection
from shemas.matriculaShema import MatriculaRegister, MatriculaUpdate, MatriculaResponse
from psycopg2.extras import RealDictCursor
from typing import List


class MatriculaDB:
    
    @staticmethod
    def insert_matricula(matricula: MatriculaRegister) -> MatriculaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO \"MATRICULA\" (\"FID_CURSO\", \"FID_ESTUDIANTE\", \"FECHA\") VALUES (%s, %s, CURRENT_DATE) RETURNING *",
                    (matricula.FID_CURSO, matricula.FID_ESTUDIANTE)
                )
                conn.commit()
                row = cursor.fetchone()
                return MatriculaResponse(**row)
    
    @staticmethod
    def get_all_matriculas() -> List[MatriculaResponse]:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"MATRICULA\"")
                rows = cursor.fetchall()
                matriculas = [MatriculaResponse(**row) for row in rows]
                return matriculas

    @staticmethod
    def get_matricula_by_id(id: int) -> MatriculaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"MATRICULA\" WHERE \"ID_MATRICULA\" = %s", (id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Matricula con ID {id} no encontrado")
                return MatriculaResponse(**row)

    @staticmethod
    def update_matricula(id: int, matricula: MatriculaUpdate) -> MatriculaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "UPDATE \"MATRICULA\" SET \"FID_CURSO\" = %s, \"FID_ESTUDIANTE\" = %s WHERE \"ID_MATRICULA\" = %s RETURNING *",
                    (matricula.FID_CURSO, matricula.FID_ESTUDIANTE, id)
                )
                conn.commit()
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Matricula con ID {id} no encontrado")
                return MatriculaResponse(**row)

    @staticmethod
    def delete_matricula(id: int) -> dict:
        with DatabaseConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM \"MATRICULA\" WHERE \"ID_MATRICULA\" = %s", (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    raise ValueError(f"Matricula con ID {id} no encontrado")
                return {"message": "Matricula eliminada exitosamente", "id": id}

        