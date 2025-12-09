from config.db import DatabaseConnection
from shemas.asignaturaShema import AsignaturaRegister, AsignaturaUpdate, AsignaturaResponse
from psycopg2.extras import RealDictCursor
from typing import List

class AsignaturaDB:

    @staticmethod
    def insert_asignatura(asignatura: AsignaturaRegister) -> AsignaturaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO \"ASIGNATURA\" (\"NOMBRE\", \"CREDITOS\") VALUES (%s, %s) RETURNING *",
                    (asignatura.NOMBRE, asignatura.CREDITOS)
                )
                conn.commit()
                row = cursor.fetchone()
                return AsignaturaResponse(**row)

    @staticmethod
    def get_all_asignaturas() -> List[AsignaturaResponse]:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"ASIGNATURA\"")
                rows = cursor.fetchall()
                asignaturas = [AsignaturaResponse(**row) for row in rows]
                return asignaturas


    @staticmethod   
    def get_asignatura_by_id(id: int) -> AsignaturaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"ASIGNATURA\" WHERE \"ID_ASIGNATURA\" = %s", (id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Asignatura con ID {id} no encontrada")
                return AsignaturaResponse(**row)

    @staticmethod
    def update_asignatura(id: int, asignatura: AsignaturaUpdate) -> AsignaturaResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "UPDATE \"ASIGNATURA\" SET \"NOMBRE\" = %s, \"CREDITOS\" = %s WHERE \"ID_ASIGNATURA\" = %s RETURNING *",
                    (asignatura.NOMBRE, asignatura.CREDITOS, id)
                )
                conn.commit()
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Asignatura con ID {id} no encontrada")
                return AsignaturaResponse(**row)

    @staticmethod
    def delete_asignatura(id: int) -> dict:
        with DatabaseConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM \"ASIGNATURA\" WHERE \"ID_ASIGNATURA\" = %s", (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    raise ValueError(f"Asignatura con ID {id} no encontrada")
                return {"message": "Asignatura eliminada exitosamente", "id": id}