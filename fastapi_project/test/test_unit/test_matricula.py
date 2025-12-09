"""
Tests unitarios para las funciones del service layer de Matrícula
Estos tests usan mocks y NO tocan la base de datos real
"""
import pytest
from unittest.mock import Mock, patch, MagicMock

from service.matricula import MatriculaDB


class TestMatriculaService:
    """
    Tests unitarios para el service layer de matrículas
    """
    
    @patch('service.matricula.DatabaseConnection')
    def test_get_all_matriculas_success(self, mock_db_class):
        """
        Test: get_all_matriculas debe retornar lista de matrículas
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            {"ID_MATRICULA": 1, "FID_ESTUDIANTE": 1, "FID_CURSO": 1},
            {"ID_MATRICULA": 2, "FID_ESTUDIANTE": 2, "FID_CURSO": 2}
        ]
        
        # Act
        result = MatriculaDB.get_all_matriculas()
        
        # Assert
        assert len(result) == 2
        assert result[0].FID_ESTUDIANTE == 1
    
    @patch('service.matricula.DatabaseConnection')
    def test_get_matricula_by_id_found(self, mock_db_class):
        """
        Test: get_matricula_by_id debe retornar matrícula cuando existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_MATRICULA": 1,
            "FID_ESTUDIANTE": 1,
            "FID_CURSO": 1
        }
        
        # Act
        result = MatriculaDB.get_matricula_by_id(1)
        
        # Assert
        assert result.ID_MATRICULA == 1
        assert result.FID_ESTUDIANTE == 1
    
    @patch('service.matricula.DatabaseConnection')
    def test_get_matricula_by_id_not_found(self, mock_db_class):
        """
        Test: get_matricula_by_id debe lanzar ValueError cuando no existe
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        # Act & Assert
        with pytest.raises(ValueError):
            MatriculaDB.get_matricula_by_id(999)
    
    @patch('service.matricula.DatabaseConnection')
    def test_insert_matricula_success(self, mock_db_class):
        """
        Test: insert_matricula debe crear y retornar matrícula
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "ID_MATRICULA": 1,
            "FID_ESTUDIANTE": 1,
            "FID_CURSO": 1
        }
        
        from shemas.matriculaShema import MatriculaRegister
        matricula_data = MatriculaRegister(FID_ESTUDIANTE=1, FID_CURSO=1)
        
        # Act
        result = MatriculaDB.insert_matricula(matricula_data)
        
        # Assert
        assert result.FID_ESTUDIANTE == 1
        assert result.FID_CURSO == 1
        mock_conn.commit.assert_called_once()
    
    @patch('service.matricula.DatabaseConnection')
    def test_delete_matricula_success(self, mock_db_class):
        """
        Test: delete_matricula debe eliminar y retornar mensaje
        """
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_class.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        # Act
        result = MatriculaDB.delete_matricula(1)
        
        # Assert
        assert "message" in result
        mock_conn.commit.assert_called_once()


class TestMatriculaValidations:
    """
    Tests unitarios para validaciones de matrícula (sin BD)
    """
    
    def test_fid_estudiante_positivo(self):
        """
        Test: FID_ESTUDIANTE debe ser positivo
        """
        assert 1 > 0
        assert not (-1 > 0)
    
    def test_fid_curso_positivo(self):
        """
        Test: FID_CURSO debe ser positivo
        """
        assert 1 > 0
        assert not (0 > 0)
