'''


'''



import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_soma(client):
    response = client.post("/soma", json={"a": 2, "b": 3})
    json_data = response.get_json()
    assert json_data["resultado"] == 5

def test_dividir(client):
    response = client.post("/dividir", json={"a": 10, "b": 2})
    json_data = response.get_json()
    assert json_data["resultado"] == 5

def test_divisao_por_zero(client):
    response = client.post("/dividir", json={"a": 10, "b": 0})
    json_data = response.get_json()
    assert response.status_code == 400
    assert "erro" in json_data