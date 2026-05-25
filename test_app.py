import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home route returns 200 and correct message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello from CI/CD Pipeline App!"
    assert data["status"] == "running"

def test_health(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_add(client):
    """Test addition endpoint."""
    response = client.get("/add/3/4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 7

def test_add_zero(client):
    """Test addition with zero."""
    response = client.get("/add/0/0")
    assert response.status_code == 200
    assert response.get_json()["result"] == 0

def test_basic_math():
    """Basic sanity check (as per task sample)."""
    assert 1 + 1 == 2
