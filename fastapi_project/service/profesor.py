from shemas.profesorShema import ProfesorRegister, ProfesorUpdate, ProfesorResponse
from config.db import DatabaseConnection
from psycopg2.extras import RealDictCursor
from typing import List

class ProfesorDB:
    @staticmethod
    def insert_profesor(profesor: ProfesorRegister) -> ProfesorResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO \"PROFESOR\" (\"NOMBRE\", \"APELLIDO\", \"EDAD\", \"GENERO\") VALUES (%s, %s, %s, %s) RETURNING *",
                    (profesor.NOMBRE, profesor.APELLIDO, profesor.EDAD, profesor.GENERO)
                )
                conn.commit()
                row = cursor.fetchone()
                return ProfesorResponse(**row)

    @staticmethod
    def get_all_profesores() -> List[ProfesorResponse]:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"PROFESOR\"")
                rows = cursor.fetchall()
                profesores = [ProfesorResponse(**row) for row in rows]
                return profesores

    @staticmethod
    def get_profesor_by_id(id: int) -> ProfesorResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"PROFESOR\" WHERE \"ID_PROFESOR\" = %s", (id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Profesor con ID {id} no encontrado")
                return ProfesorResponse(**row)

    @staticmethod
    def update_profesor(id: int, profesor: ProfesorUpdate) -> ProfesorResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "UPDATE \"PROFESOR\" SET \"NOMBRE\" = %s, \"APELLIDO\" = %s, \"EDAD\" = %s, \"GENERO\" = %s WHERE \"ID_PROFESOR\" = %s RETURNING *",
                    (profesor.NOMBRE, profesor.APELLIDO, profesor.EDAD, profesor.GENERO, id)
                )
                conn.commit()
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Profesor con ID {id} no encontrado")
                return ProfesorResponse(**row)

    @staticmethod
    def delete_profesor(id: int) -> dict:
        with DatabaseConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM \"PROFESOR\" WHERE \"ID_PROFESOR\" = %s", (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    raise ValueError(f"Profesor con ID {id} no encontrado")
                return {"message": "Profesor eliminado exitosamente", "id": id}
