from conftest import profesor_data

def test_create_profesor(client, profesor_data):
    res = client.post("/profesores/register", json=profesor_data)
    assert res.status_code == 201
    item = res.json()
    assert item["NOMBRE"] == profesor_data["NOMBRE"]

def test_get_all_profesores(client):
    res = client.get("/profesores/all")
    assert res.status_code == 200
    items = res.json()
    assert len(items) > 0

def test_get_profesor_by_id(client):
    res = client.get("/profesores/1")
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Juan" # Dato del insert.sql

def test_update_profesor(client):
    res = client.put("/profesores/update/1", json={"NOMBRE": "Juan Updated", "APELLIDO": "Perez", "EDAD": 21, "GENERO": "M"})
    assert res.status_code == 200
    item = res.json()
    assert item["NOMBRE"] == "Juan Updated"

def test_delete_profesor(client):
    # Crear uno para borrar
    new_profesor = {"NOMBRE": "To Delete", "APELLIDO": "Prof", "EDAD": 30, "GENERO": "M"}
    create_res = client.post("/profesores/register", json=new_profesor)
    assert create_res.status_code == 201
    id_to_delete = create_res.json()["ID_PROFESOR"]

    res = client.delete(f"/profesores/delete/{id_to_delete}")
    assert res.status_code == 200
    item = res.json()
    assert item["message"] == "Profesor eliminado exitosamente"

def test_get_profesor_by_id_not_found(client):
    res = client.get("/profesores/9999")
    assert res.status_code == 404

def test_update_profesor_not_found(client):
    res = client.put("/profesores/update/9999", json={"NOMBRE": "Ghost", "APELLIDO": "Ghost", "EDAD": 30, "GENERO": "M"})
    assert res.status_code == 404

def test_delete_profesor_not_found(client):
    res = client.delete("/profesores/delete/9999")
    assert res.status_code == 404
