from conftest import curso_data

def test_create_curso(client, curso_data):
    res = client.post("/cursos/register", json=curso_data)
    assert res.status_code == 201
    item = res.json()
    assert item["NOMBRE"] == curso_data["NOMBRE"]

def test_get_all_cursos(client):
    res = client.get("/cursos/all")
    assert res.status_code == 200
    items = res.json()
    assert len(items) > 0

def test_get_curso_by_id(client):
    res = client.get("/cursos/1")
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Matematicas" # Dato del insert.sql

def test_update_curso(client):
    # Actualizar curso 1
    res = client.put("/cursos/update/1", json={"NOMBRE": "Matematicas Avanzadas", "FID_ASIGNATURA": 1, "FID_PROFESOR": 1})
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Matematicas Avanzadas"

def test_delete_curso(client):
    # Crear uno para borrar
    new_curso = {"NOMBRE": "To Delete", "FID_ASIGNATURA": 1, "FID_PROFESOR": 1}
    create_res = client.post("/cursos/register", json=new_curso)
    assert create_res.status_code == 201
    id_to_delete = create_res.json()["ID_CURSO"]

    res = client.delete(f"/cursos/delete/{id_to_delete}")
    assert res.status_code == 200
    item = res.json()
    assert item["message"] == "Curso eliminado exitosamente"

def test_get_curso_by_id_not_found(client):
    res = client.get("/cursos/9999")
    assert res.status_code == 404

def test_update_curso_not_found(client):
    res = client.put("/cursos/update/9999", json={"NOMBRE": "Ghost", "FID_ASIGNATURA": 1, "FID_PROFESOR": 1})
    assert res.status_code == 404

def test_delete_curso_not_found(client):
    res = client.delete("/cursos/delete/9999")
    assert res.status_code == 404
