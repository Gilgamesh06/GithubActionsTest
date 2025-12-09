from conftest import matricula_data

def test_create_matricula(client, matricula_data):
    # Matricula requiere IDs validos. Usamos 1 y 1 que sabemos existen por insert.sql
    # Pero matricula_data ya tiene 1 y 1.
    res = client.post("/matriculas/register", json=matricula_data)
    assert res.status_code == 201
    item = res.json()
    assert item["FID_ESTUDIANTE"] == matricula_data["FID_ESTUDIANTE"]

def test_get_all_matriculas(client):
    res = client.get("/matriculas/all")
    assert res.status_code == 200
    items = res.json()
    assert len(items) > 0

def test_get_matricula_by_id(client):
    res = client.get("/matriculas/1")
    assert res.status_code == 200
    item = res.json()
    assert item["FID_ESTUDIANTE"] == 1

def test_update_matricula(client):
    # Actualizar matricula 1. Cambiamos curso a 2
    res = client.put("/matriculas/update/1", json={"FID_ESTUDIANTE": 1, "FID_CURSO": 2})
    assert res.status_code == 200
    item = res.json()
    assert item["FID_CURSO"] == 2

def test_delete_matricula(client):
    # Crear uno para borrar
    new_matricula = {"FID_ESTUDIANTE": 2, "FID_CURSO": 2}
    create_res = client.post("/matriculas/register", json=new_matricula)
    assert create_res.status_code == 201
    id_to_delete = create_res.json()["ID_MATRICULA"]

    res = client.delete(f"/matriculas/delete/{id_to_delete}")
    assert res.status_code == 200
    item = res.json()
    assert item["message"] == "Matricula eliminada exitosamente"

def test_get_matricula_by_id_not_found(client):
    res = client.get("/matriculas/9999")
    assert res.status_code == 404

def test_update_matricula_not_found(client):
    res = client.put("/matriculas/update/9999", json={"FID_ESTUDIANTE": 1, "FID_CURSO": 1})
    assert res.status_code == 404

def test_delete_matricula_not_found(client):
    res = client.delete("/matriculas/delete/9999")
    assert res.status_code == 404
