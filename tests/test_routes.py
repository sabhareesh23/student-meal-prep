import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_all_meals(client):
    response = client.get("/api/meals")
    assert response.status_code == 200
    assert response.is_json is True

def test_get_monday_meals(client):
    response = client.get("/api/meals/monday")
    assert response.status_code == 200

def test_invalid_day(client):
    response = client.get("/api/meals/notaday")
    assert response.status_code == 404