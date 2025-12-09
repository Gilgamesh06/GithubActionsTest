# Tests Unitarios - FastAPI Project

## Descripción

Suite completa de **tests unitarios verdaderos** para el service layer de la API FastAPI. Estos tests usan **mocks** y **NO tocan la base de datos real**.

## ¿Qué son Tests Unitarios?

Los tests unitarios prueban funciones o métodos de forma **aislada**, usando:
- ✅ **Mocks**: Simulan dependencias externas (base de datos, APIs, etc.)
- ✅ **Fixtures**: Proveen datos de prueba predefinidos
- ✅ **Sin BD**: No requieren base de datos real
- ✅ **Rápidos**: Se ejecutan en milisegundos
- ✅ **Aislados**: Cada test es independiente

## Estructura de Tests

```
test/
├── __init__.py
├── conftest.py              # Fixtures compartidos y mocks
├── test_estudiante.py       # Tests unitarios de estudiante
├── test_profesor.py         # Tests unitarios de profesor
├── test_asignatura.py       # Tests unitarios de asignatura
├── test_curso.py            # Tests unitarios de curso
└── test_matricula.py        # Tests unitarios de matrícula
```

## Cobertura de Tests

Cada archivo de test incluye:

### Tests del Service Layer
- ✅ **get_all_*()** - Obtener todos los registros (con mock de BD)
- ✅ **get_*_by_id()** - Obtener por ID (casos: encontrado, no encontrado)
- ✅ **insert_*()** - Crear registro (con mock de commit)
- ✅ **update_*()** - Actualizar registro (casos: éxito, no encontrado)
- ✅ **delete_*()** - Eliminar registro (casos: éxito, no encontrado)

### Tests de Validaciones
- ✅ Validación de rangos (edad, créditos, etc.)
- ✅ Validación de longitud de strings
- ✅ Validación de valores positivos
- ✅ Validación de campos no vacíos

## Total de Tests

| Entidad | Tests Service Layer | Tests Validaciones | Total |
|---------|-------------------|-------------------|-------|
| Estudiante | 10 | 3 | 13 |
| Profesor | 6 | 2 | 8 |
| Asignatura | 7 | 2 | 9 |
| Curso | 5 | 2 | 7 |
| Matrícula | 5 | 2 | 7 |
| **TOTAL** | **33** | **11** | **44** |

## Requisitos

```bash
pip install pytest pytest-cov
```

**Nota:** No se requiere `httpx` porque estos son tests unitarios del service layer, no tests de endpoints.

## Ejecutar Tests

### Todos los tests
```bash
pytest
```

### Tests con verbose
```bash
pytest -v
```

### Tests de una entidad específica
```bash
pytest test/test_estudiante.py -v
pytest test/test_profesor.py -v
```

### Con cobertura
```bash
pytest --cov=service --cov-report=html
```

## Ejemplo de Test Unitario con Mock

```python
@patch('service.estudiante.DatabaseConnection')
def test_get_estudiante_by_id_found(mock_db_class):
    # Arrange - Configurar mocks
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_db_class.return_value.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Simular respuesta de la BD
    mock_cursor.fetchone.return_value = {
        "ID_ESTUDIANTE": 1,
        "NOMBRE": "Juan",
        "APELLIDO": "Pérez",
        "EDAD": 20,
        "GENERO": "M"
    }
    
    # Act - Ejecutar función
    result = EstudianteDB.get_estudiante_by_id(1)
    
    # Assert - Verificar resultados
    assert result.ID_ESTUDIANTE == 1
    assert result.NOMBRE == "Juan"
```

## Ventajas de Tests Unitarios con Mocks

### ✅ Sin Base de Datos
- No requiere BD configurada
- No hay datos de prueba en producción
- No hay conflictos con otros tests

### ✅ Rápidos
- Se ejecutan en milisegundos
- Ideales para CI/CD
- Feedback inmediato

### ✅ Aislados
- Prueban una función a la vez
- No dependen de otros componentes
- Fácil identificar errores

### ✅ Controlados
- Puedes simular cualquier escenario
- Casos de error fáciles de probar
- Resultados predecibles

## Diferencia con Tests de Integración

| Aspecto | Tests Unitarios | Tests de Integración |
|---------|----------------|---------------------|
| **Base de Datos** | ❌ Mock | ✅ Real |
| **Velocidad** | ⚡ Muy rápido | 🐌 Lento |
| **Alcance** | 🎯 Una función | 🌐 Flujo completo |
| **Dependencias** | 🔌 Mockeadas | 🔗 Reales |
| **Propósito** | Lógica de negocio | Integración de componentes |

## Comandos Útiles

```bash
# Ejecutar solo tests que fallaron
pytest --lf

# Detener en el primer fallo
pytest -x

# Mostrar print statements
pytest -s

# Tests más lentos
pytest --durations=10

# Generar reporte XML (para CI/CD)
pytest --junitxml=report.xml

# Cobertura solo del service layer
pytest --cov=service --cov-report=term-missing
```

## Notas Importantes

### ✅ Ventajas
- **No requiere base de datos** - Pueden ejecutarse en cualquier ambiente
- **Rápidos** - Ideales para desarrollo iterativo
- **Seguros** - No modifican datos reales
- **Portables** - Funcionan en cualquier máquina

### 📝 Limitaciones
- No prueban la integración con la BD real
- No detectan problemas de SQL
- No validan constraints de BD
- Requieren tests de integración complementarios

## Recomendación

Para una cobertura completa, combinar:
1. **Tests Unitarios** (estos) - Lógica de negocio
2. **Tests de Integración** - Integración con BD
3. **Tests End-to-End** - Flujos completos de usuario


## Estructura de Tests

```
test/
├── __init__.py
├── conftest.py              # Fixtures compartidos
├── test_estudiante.py       # Tests de estudiantes
├── test_profesor.py         # Tests de profesores
├── test_asignatura.py       # Tests de asignaturas
├── test_curso.py            # Tests de cursos
└── test_matricula.py        # Tests de matrículas
```

## Cobertura de Tests

Cada archivo de test incluye:

### Tests de Endpoints (CRUD)
- ✅ **POST /register** - Crear registro con datos válidos
- ✅ **GET /all** - Obtener todos los registros
- ✅ **GET /{id}** - Obtener registro por ID (existente y no existente)
- ✅ **PUT /update/{id}** - Actualizar registro (existente y no existente)
- ✅ **DELETE /delete/{id}** - Eliminar registro (existente y no existente)

### Tests de Validaciones
- ✅ Validación de campos requeridos
- ✅ Validación de rangos (edad, créditos, etc.)
- ✅ Validación de longitud de strings
- ✅ Validación de enums (género)
- ✅ Validación de foreign keys
- ✅ Limpieza de espacios en blanco

### Tests de Casos de Error
- ✅ Datos inválidos (422 Unprocessable Entity)
- ✅ Recursos no encontrados (404 Not Found)
- ✅ Violaciones de integridad (409 Conflict)

## Total de Tests

| Entidad | Tests de Endpoints | Tests de Validaciones | Total |
|---------|-------------------|----------------------|-------|
| Estudiante | 10 | 3 | 13 |
| Profesor | 9 | 2 | 11 |
| Asignatura | 10 | 3 | 13 |
| Curso | 9 | 2 | 11 |
| Matrícula | 9 | 2 | 11 |
| **TOTAL** | **47** | **12** | **59** |

## Requisitos

```bash
pip install pytest pytest-cov httpx
```

## Ejecutar Tests

### Todos los tests
```bash
pytest
```

### Tests con cobertura
```bash
pytest --cov=. --cov-report=html
```

### Tests de una entidad específica
```bash
pytest test/test_estudiante.py
pytest test/test_profesor.py
pytest test/test_asignatura.py
pytest test/test_curso.py
pytest test/test_matricula.py
```

### Tests con output verbose
```bash
pytest -v
```

### Tests con output detallado
```bash
pytest -vv
```

### Tests con print statements
```bash
pytest -s
```

## Fixtures Disponibles

Definidos en `conftest.py`:

- **client**: Cliente de prueba FastAPI TestClient
- **estudiante_data**: Datos válidos de estudiante
- **profesor_data**: Datos válidos de profesor
- **asignatura_data**: Datos válidos de asignatura
- **curso_data**: Datos válidos de curso
- **matricula_data**: Datos válidos de matrícula

## Ejemplo de Uso

```python
def test_example(client, estudiante_data):
    # Usar el cliente para hacer requests
    response = client.post("/estudiantes/register", json=estudiante_data)
    
    # Verificar respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["NOMBRE"] == estudiante_data["NOMBRE"]
```

## Notas Importantes

### Base de Datos
- Los tests usan la misma base de datos que la aplicación
- **IMPORTANTE**: Ejecutar tests en un ambiente de desarrollo/testing
- NO ejecutar tests en producción

### Orden de Ejecución
- Los tests son independientes entre sí
- Cada test crea sus propios datos de prueba
- No hay dependencias entre tests

### Limpieza
- Los tests NO limpian automáticamente los datos creados
- Considerar usar una base de datos de prueba separada
- O implementar fixtures de limpieza si es necesario

## Mejoras Futuras

- [ ] Usar base de datos de prueba separada
- [ ] Implementar fixtures de limpieza automática
- [ ] Agregar tests de integración
- [ ] Agregar tests de performance
- [ ] Implementar mocking para dependencias externas
- [ ] Agregar tests de seguridad
- [ ] Configurar CI/CD para ejecutar tests automáticamente

## Comandos Útiles

```bash
# Ejecutar solo tests que fallaron la última vez
pytest --lf

# Ejecutar tests en paralelo (requiere pytest-xdist)
pytest -n auto

# Generar reporte de cobertura en terminal
pytest --cov=. --cov-report=term-missing

# Ejecutar tests con markers específicos
pytest -m "slow"  # Si defines markers

# Detener en el primer fallo
pytest -x

# Mostrar los tests más lentos
pytest --durations=10
```
