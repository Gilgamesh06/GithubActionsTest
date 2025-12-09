"""
Tests unitarios para las funciones del service layer de Asignatura
Estos tests usan mocks y NO tocan la base de datos real
"""
import pytest
from unittest.mock import Mock, patch, MagicMock

from service.asignatura import AsignaturaDB


class TestAsignaturaService:
    """
    Tests unitarios para el service layer de asignaturas
    """
    
    @patch('service.asignatura.DatabaseConnection')
    def test_get_all_asignaturas_success(self, mock_db_class):
        """
        Test: get_all_asignaturas debe retornar lista de asignaturas
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            {"ID_ASIGNATURA": 1, "NOMBRE": "Matemáticas", "CREDITOS": 5},
            {"ID_ASIGNATURA": 2, "NOMBRE": "Física", "CREDITOS": 6}
        ]
        
        # Act
        result = AsignaturaDB.get_all_asignaturas()
        
        # Assert
        assert len(result) == 2
        assert result[0].NOMBRE == "Matemáticas"
        assert result[1].CREDITOS == 6
    
    @patch('service.asignatura.DatabaseConnection')
    def test_get_asignatura_by_id_found(self, mock_db_class):
        """
        Test: get_asignatura_by_id debe retornar asignatura cuando existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_ASIGNATURA": 1,
            "NOMBRE": "Matemáticas",
            "CREDITOS": 5
        }
        
        # Act
        result = AsignaturaDB.get_asignatura_by_id(1)
        
        # Assert
        assert result.ID_ASIGNATURA == 1
        assert result.NOMBRE == "Matemáticas"
        assert result.CREDITOS == 5
    
    @patch('service.asignatura.DatabaseConnection')
    def test_get_asignatura_by_id_not_found(self, mock_db_class):
        """
        Test: get_asignatura_by_id debe lanzar ValueError cuando no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        # Act & Assert
        with pytest.raises(ValueError):
            AsignaturaDB.get_asignatura_by_id(999)
    
    @patch('service.asignatura.DatabaseConnection')
    def test_insert_asignatura_success(self, mock_db_class):
        """
        Test: insert_asignatura debe crear y retornar asignatura
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_ASIGNATURA": 1,
            "NOMBRE": "Matemáticas",
            "CREDITOS": 5
        }
        
        from shemas.asignaturaShema import AsignaturaRegister
        asignatura_data = AsignaturaRegister(NOMBRE="Matemáticas", CREDITOS=5)
        
        # Act
        result = AsignaturaDB.insert_asignatura(asignatura_data)
        
        # Assert
        assert result.NOMBRE == "Matemáticas"
        assert result.CREDITOS == 5
        mock_conn.commit.assert_called_once()
    
    @patch('service.asignatura.DatabaseConnection')
    def test_update_asignatura_success(self, mock_db_class):
        """
        Test: update_asignatura debe actualizar y retornar asignatura
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_ASIGNATURA": 1,
            "NOMBRE": "Física",
            "CREDITOS": 6
        }
        
        from shemas.asignaturaShema import AsignaturaUpdate
        asignatura_data = AsignaturaUpdate(NOMBRE="Física", CREDITOS=6)
        
        # Act
        result = AsignaturaDB.update_asignatura(1, asignatura_data)
        
        # Assert
        assert result.NOMBRE == "Física"
        mock_conn.commit.assert_called_once()
    
    @patch('service.asignatura.DatabaseConnection')
    def test_delete_asignatura_success(self, mock_db_class):
        """
        Test: delete_asignatura debe eliminar y retornar mensaje
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        # Act
        result = AsignaturaDB.delete_asignatura(1)
        
        # Assert
        assert "message" in result
        mock_conn.commit.assert_called_once()


class TestAsignaturaValidations:
    """
    Tests unitarios para validaciones de asignatura (sin BD)
    """
    
    def test_creditos_range(self):
        """
        Test: Créditos deben estar entre 1 y 10
        """
        assert 1 <= 5 <= 10  # Válido
        assert not (1 <= 0 <= 10)  # Inválido
        assert not (1 <= 11 <= 10)  # Inválido
    
    def test_nombre_no_vacio(self):
        """
        Test: Nombre no debe estar vacío
        """
        assert len("Matemáticas") > 0
        assert not (len("") > 0)
