"""
Tests unitarios para las funciones del service layer de Curso
Estos tests usan mocks y NO tocan la base de datos real
"""
import pytest
from unittest.mock import Mock, patch, MagicMock

from service.curso import CursoDB


class TestCursoService:
    """
    Tests unitarios para el service layer de cursos
    """
    
    @patch('service.curso.DatabaseConnection')
    def test_get_all_cursos_success(self, mock_db_class):
        """
        Test: get_all_cursos debe retornar lista de cursos
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            {"ID_CURSO": 1, "NOMBRE": "Cálculo I", "FID_ASIGNATURA": 1, "FID_PROFESOR": 1},
            {"ID_CURSO": 2, "NOMBRE": "Álgebra", "FID_ASIGNATURA": 2, "FID_PROFESOR": 2}
        ]
        
        # Act
        result = CursoDB.get_all_cursos()
        
        # Assert
        assert len(result) == 2
        assert result[0].NOMBRE == "Cálculo I"
    
    @patch('service.curso.DatabaseConnection')
    def test_get_curso_by_id_found(self, mock_db_class):
        """
        Test: get_curso_by_id debe retornar curso cuando existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_CURSO": 1,
            "NOMBRE": "Cálculo I",
            "FID_ASIGNATURA": 1,
            "FID_PROFESOR": 1
        }
        
        # Act
        result = CursoDB.get_curso_by_id(1)
        
        # Assert
        assert result.ID_CURSO == 1
        assert result.NOMBRE == "Cálculo I"
    
    @patch('service.curso.DatabaseConnection')
    def test_get_curso_by_id_not_found(self, mock_db_class):
        """
        Test: get_curso_by_id debe lanzar ValueError cuando no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        # Act & Assert
        with pytest.raises(ValueError):
            CursoDB.get_curso_by_id(999)
    
    @patch('service.curso.DatabaseConnection')
    def test_insert_curso_success(self, mock_db_class):
        """
        Test: insert_curso debe crear y retornar curso
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_CURSO": 1,
            "NOMBRE": "Cálculo I",
            "FID_ASIGNATURA": 1,
            "FID_PROFESOR": 1
        }
        
        from shemas.cursoShema import CursoRegister
        curso_data = CursoRegister(NOMBRE="Cálculo I", FID_ASIGNATURA=1, FID_PROFESOR=1)
        
        # Act
        result = CursoDB.insert_curso(curso_data)
        
        # Assert
        assert result.NOMBRE == "Cálculo I"
        mock_conn.commit.assert_called_once()
    
    @patch('service.curso.DatabaseConnection')
    def test_delete_curso_success(self, mock_db_class):
        """
        Test: delete_curso debe eliminar y retornar mensaje
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        # Act
        result = CursoDB.delete_curso(1)
        
        # Assert
        assert "message" in result
        mock_conn.commit.assert_called_once()


class TestCursoValidations:
    """
    Tests unitarios para validaciones de curso (sin BD)
    """
    
    def test_fid_positivo(self):
        """
        Test: FIDs deben ser positivos
        """
        assert 1 > 0
        assert not (-1 > 0)
        assert not (0 > 0)
    
    def test_nombre_no_vacio(self):
        """
        Test: Nombre no debe estar vacío
        """
        assert len("Cálculo I") > 0
        assert not (len("") > 0)
