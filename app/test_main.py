from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_write_main():
    response = client.post("/", headers={}, json={"msg": "Hello World"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_update_main():
    response = client.patch("/", headers={}, json={"msg": "Hello World"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World Update"}


def test_delete_main():
    response = client.delete("/1", headers={})
    assert response.status_code == 200
    assert response.json() == {"msg": "1"}
