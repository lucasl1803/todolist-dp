from fastapi.testclient import TestClient
from main import app
from database import Base, engine


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create_category_and_task():
   
    resp_cat = client.post("/categories/", json={"name": "Estudos"})
    assert resp_cat.status_code == 200
    cat_id = resp_cat.json()["id"]


    resp_task = client.post(
        "/tasks/",
        json={
            "title": "Tarefa de teste",
            "description": "Descrição qualquer",
            "status": "TODO",
            "category_id": cat_id,
            "due_date": "2025-11-20"
        },
    )

    assert resp_task.status_code == 200
    data = resp_task.json()
    assert data["title"] == "Tarefa de teste"
    assert data["category"]["id"] == cat_id
