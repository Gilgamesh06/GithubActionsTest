# tests/test_api.py

def test_create_estudiante(client, estudiante_data):
    res = client.post("/estudiantes/register", json=estudiante_data)
    assert res.status_code == 201
    item = res.json()
    assert item["NOMBRE"] == estudiante_data["NOMBRE"]


def test_get_all_estudiantes(client):
    res = client.get("/estudiantes/all")
    assert res.status_code == 200
    items = res.json()
    assert len(items) > 0

def test_get_estudiante_by_id(client):
    res = client.get("/estudiantes/1")
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Juan"

def test_update_estudiante(client):
    res = client.put("/estudiantes/1", json={"NOMBRE": "Juan", "APELLIDO": "Pérez", "EDAD": 20, "GENERO": "M"})
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Juan"

def test_delete_estudiante(client):
    res = client.delete("/estudiantes/6")
    assert res.status_code == 200
    item = res.json()
    assert item["message"] == "Estudiante eliminado exitosamente"


def test_get_estudiante_by_id_not_found(client):
    res = client.get("/estudiantes/6")
    assert res.status_code == 404

def test_update_estudiante_not_found(client):
    res = client.put("/estudiantes/6", json={"NOMBRE": "Juan", "APELLIDO": "Pérez", "EDAD": 20, "GENERO": "M"})
    assert res.status_code == 404

def test_delete_estudiante_not_found(client):
    res = client.delete("/estudiantes/6")
    assert res.status_code == 404


def test_delete_estudiante_with_dependencias(client):
    res = client.delete("/estudiantes/1")
    assert res.status_code == 409
    item = res.json()
    assert item["detail"] == "No se puede eliminar: el estudiante tiene registros relacionados"



