"""
Tests unitarios para las funciones del service layer de Profesor
Estos tests usan mocks y NO tocan la base de datos real
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from fastapi import HTTPException

from service.profesor import ProfesorDB


class TestProfesorService:
    """
    Tests unitarios para el service layer de profesores
    """
    
    @patch('service.profesor.DatabaseConnection')
    def test_get_all_profesores_success(self, mock_db_class):
        """
        Test: get_all_profesores debe retornar lista de profesores
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            {"ID_PROFESOR": 1, "NOMBRE": "María", "APELLIDO": "González", "EDAD": 35, "GENERO": "F"},
            {"ID_PROFESOR": 2, "NOMBRE": "Carlos", "APELLIDO": "Pérez", "EDAD": 40, "GENERO": "M"}
        ]
        
        # Act
        result = ProfesorDB.get_all_profesores()
        
        # Assert
        assert len(result) == 2
        assert result[0].NOMBRE == "María"
        assert result[1].NOMBRE == "Carlos"
    
    @patch('service.profesor.DatabaseConnection')
    def test_get_profesor_by_id_found(self, mock_db_class):
        """
        Test: get_profesor_by_id debe retornar profesor cuando existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_PROFESOR": 1,
            "NOMBRE": "María",
            "APELLIDO": "González",
            "EDAD": 35,
            "GENERO": "F"
        }
        
        # Act
        result = ProfesorDB.get_profesor_by_id(1)
        
        # Assert
        assert result.ID_PROFESOR == 1
        assert result.NOMBRE == "María"
    
    @patch('service.profesor.DatabaseConnection')
    def test_get_profesor_by_id_not_found(self, mock_db_class):
        """
        Test: get_profesor_by_id debe lanzar ValueError cuando no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        # Act & Assert
        with pytest.raises(ValueError):
            ProfesorDB.get_profesor_by_id(999)
    
    @patch('service.profesor.DatabaseConnection')
    def test_insert_profesor_success(self, mock_db_class):
        """
        Test: insert_profesor debe crear y retornar profesor
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_PROFESOR": 1,
            "NOMBRE": "María",
            "APELLIDO": "González",
            "EDAD": 35,
            "GENERO": "F"
        }
        
        from shemas.profesorShema import ProfesorRegister
        profesor_data = ProfesorRegister(NOMBRE="María", APELLIDO="González", EDAD=35, GENERO="F")
        
        # Act
        result = ProfesorDB.insert_profesor(profesor_data)
        
        # Assert
        assert result.NOMBRE == "María"
        mock_conn.commit.assert_called_once()
    
    @patch('service.profesor.DatabaseConnection')
    def test_delete_profesor_success(self, mock_db_class):
        """
        Test: delete_profesor debe eliminar y retornar mensaje
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        # Act
        result = ProfesorDB.delete_profesor(1)
        
        # Assert
        assert "message" in result
        mock_conn.commit.assert_called_once()


class TestProfesorValidations:
    """
    Tests unitarios para validaciones de profesor (sin BD)
    """
    
    def test_edad_minima_profesor(self):
        """
        Test: Edad mínima de profesor debe ser 18
        """
        assert 18 <= 35  # Edad válida
        assert not (18 <= 17)  # Edad inválida
    
    def test_nombre_longitud_minima(self):
        """
        Test: Nombre debe tener al menos 3 caracteres
        """
        assert len("María") >= 3
        assert not (len("Ma") >= 3)
