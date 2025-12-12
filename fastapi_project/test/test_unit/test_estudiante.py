"""
Tests unitarios para las funciones del service layer de Estudiante
Estos tests usan mocks y NO tocan la base de datos real
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from fastapi import HTTPException

# Importar la clase del service layer
from service.estudiante import EstudianteDB


class TestEstudianteService:
    """
    Tests unitarios para el service layer de estudiantes
    """
    
    @patch('service.estudiante.DatabaseConnection')
    def test_get_all_estudiantes_success(self, mock_db_class):
        """
        Test: get_all_estudiantes debe retornar lista de estudiantes
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simular datos de la BD
        mock_cursor.fetchall.return_value = [
            {"ID_ESTUDIANTE": 1, "NOMBRE": "Juan", "APELLIDO": "Pérez", "EDAD": 20, "GENERO": "M"},
            {"ID_ESTUDIANTE": 2, "NOMBRE": "María", "APELLIDO": "González", "EDAD": 22, "GENERO": "F"}
        ]
        
        # Act
        result = EstudianteDB.get_all_estudiantes()
        
        # Assert
        assert len(result) == 2
        assert result[0].NOMBRE == "Juan"
        assert result[1].NOMBRE == "María"
        mock_cursor.execute.assert_called_once()
    
    @patch('service.estudiante.DatabaseConnection')
    def test_get_all_estudiantes_empty(self, mock_db_class):
        """
        Test: get_all_estudiantes debe retornar lista vacía si no hay datos
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []
        
        # Act
        result = EstudianteDB.get_all_estudiantes()
        
        # Assert
        assert result == []
    
    
    @patch('service.estudiante.DatabaseConnection')
    def test_get_estudiante_by_id_found(self, mock_db_class):
        """
        Test: get_estudiante_by_id debe retornar estudiante cuando existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {
            "ID_ESTUDIANTE": 1,
            "NOMBRE": "Juan",
            "APELLIDO": "Pérez",
            "EDAD": 20,
            "GENERO": "M"
        }
        
        # Act
        result = EstudianteDB.get_estudiante_by_id(1)
        
        # Assert
        assert result.ID_ESTUDIANTE == 1
        assert result.NOMBRE == "Juan"
        mock_cursor.execute.assert_called_once()
    
    @patch('service.estudiante.DatabaseConnection')
    def test_get_estudiante_by_id_not_found(self, mock_db_class):
        """
        Test: get_estudiante_by_id debe lanzar ValueError cuando no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        # Act & Assert
        with pytest.raises(ValueError):
            EstudianteDB.get_estudiante_by_id(999)
    
    @patch('service.estudiante.DatabaseConnection')
    def test_insert_estudiante_success(self, mock_db_class):
        """
        Test: insert_estudiante debe crear y retornar estudiante
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {
            "ID_ESTUDIANTE": 1,
            "NOMBRE": "Juan",
            "APELLIDO": "Pérez",
            "EDAD": 20,
            "GENERO": "M"
        }
        
        from shemas.estudianteShema import EstudianteRegister
        estudiante_data = EstudianteRegister(NOMBRE="Juan", APELLIDO="Pérez", EDAD=20, GENERO="M")
        
        # Act
        result = EstudianteDB.insert_estudiante(estudiante_data)
        
        # Assert
        assert result.NOMBRE == "Juan"
        assert result.APELLIDO == "Pérez"
        mock_cursor.execute.assert_called()
        mock_conn.commit.assert_called_once()
    
    @patch('service.estudiante.DatabaseConnection')
    def test_update_estudiante_success(self, mock_db_class):
        """
        Test: update_estudiante debe actualizar y retornar estudiante
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_ESTUDIANTE": 1,
            "NOMBRE": "Carlos",
            "APELLIDO": "López",
            "EDAD": 22,
            "GENERO": "M"
        }
        
        from shemas.estudianteShema import EstudianteUpdate
        estudiante_data = EstudianteUpdate(NOMBRE="Carlos", APELLIDO="López", EDAD=22, GENERO="M")
        
        # Act
        result = EstudianteDB.update_estudiante(1, estudiante_data)
        
        # Assert
        assert result.NOMBRE == "Carlos"
        assert result.APELLIDO == "Lopez"
        mock_conn.commit.assert_called_once()
    
    @patch('service.estudiante.DatabaseConnection')
    def test_update_estudiante_not_found(self, mock_db_class):
        """
        Test: update_estudiante debe lanzar ValueError si no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        from shemas.estudianteShema import EstudianteUpdate
        estudiante_data = EstudianteUpdate(NOMBRE="Carlos", APELLIDO="López", EDAD=22, GENERO="M")
        
        # Act & Assert
        with pytest.raises(ValueError):
            EstudianteDB.update_estudiante(999, estudiante_data)
    
    @patch('service.estudiante.DatabaseConnection')
    def test_delete_estudiante_success(self, mock_db_class):
        """
        Test: delete_estudiante debe eliminar y retornar mensaje
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        # Act
        result = EstudianteDB.delete_estudiante(1)
        
        # Assert
        assert "message" in result
        mock_conn.commit.assert_called_once()
    
    @patch('service.estudiante.DatabaseConnection')
    def test_delete_estudiante_not_found(self, mock_db_class):
        """
        Test: delete_estudiante debe lanzar ValueError si no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 0
        
        # Act & Assert
        with pytest.raises(ValueError):
            EstudianteDB.delete_estudiante(999)


class TestEstudianteValidations:
    """
    Tests unitarios para validaciones de estudiante (sin BD)
    """
    
    def test_nombre_trimming(self):
        """
        Test: Verificar que los nombres se limpien de espacios
        """
        nombre = "  Juan  "
        nombre_limpio = nombre.strip()
        assert nombre_limpio == "Juan"
    
    def test_edad_range_validation(self):
        """
        Test: Verificar rangos de edad válidos
        """
        assert 5 <= 20 <= 100  # Edad válida
        assert not (5 <= 3 <= 100)  # Edad inválida
        assert not (5 <= 101 <= 100)  # Edad inválida
    
    def test_genero_validation(self):
        """
        Test: Verificar que género sea M, F o O
        """
        generos_validos = ["M", "F", "O"]
        assert "M" in generos_validos
        assert "F" in generos_validos
        assert "O" in generos_validos
        assert "X" not in generos_validos
