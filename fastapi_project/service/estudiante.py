from shemas.estudianteShema import EstudianteRegister, EstudianteUpdate, EstudianteResponse
from config.db import DatabaseConnection
from psycopg2.extras import RealDictCursor
from typing import List

class EstudianteDB:
    @staticmethod
    def insert_estudiante(estudiante: EstudianteRegister) -> EstudianteResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "INSERT INTO \"ESTUDIANTE\" (\"NOMBRE\", \"APELLIDO\", \"EDAD\", \"GENERO\") VALUES (%s, %s, %s, %s) RETURNING *",
                    (estudiante.NOMBRE, estudiante.APELLIDO, estudiante.EDAD, estudiante.GENERO)
                )
                conn.commit()
                row = cursor.fetchone()
                return EstudianteResponse(**row)



    @staticmethod
    def get_all_estudiantes() -> List[EstudianteResponse]:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"ESTUDIANTE\"")
                rows = cursor.fetchall()
                estudiantes = [EstudianteResponse(**row) for row in rows]            
                return estudiantes

            
    @staticmethod
    def get_estudiante_by_id(id: int) -> EstudianteResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM \"ESTUDIANTE\" WHERE \"ID_ESTUDIANTE\" = %s", (id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Estudiante con ID {id} no encontrado")
                return EstudianteResponse(**row)

    @staticmethod
    def update_estudiante(id: int, estudiante: EstudianteUpdate) -> EstudianteResponse:
        with DatabaseConnection(cursor_factory=RealDictCursor) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "UPDATE \"ESTUDIANTE\" SET \"NOMBRE\" = %s, \"APELLIDO\" = %s, \"EDAD\" = %s, \"GENERO\" = %s WHERE \"ID_ESTUDIANTE\" = %s RETURNING *",
                    (estudiante.NOMBRE, estudiante.APELLIDO, estudiante.EDAD, estudiante.GENERO, id)
                )
                conn.commit()
                row = cursor.fetchone()
                if row is None:
                    raise ValueError(f"Estudiante con ID {id} no encontrado")
                return EstudianteResponse(**row)

    @staticmethod
    def delete_estudiante(id: int) -> dict:
        with DatabaseConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM \"ESTUDIANTE\" WHERE \"ID_ESTUDIANTE\" = %s", (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    raise ValueError(f"Estudiante con ID {id} no encontrado")
                return {"message": "Estudiante eliminado exitosamente", "id": id}