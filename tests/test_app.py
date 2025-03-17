import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_task(client):
    data = {'title': 'Tarea de prueba', 'description': 'Descripción de prueba'}
    response = client.post('/tasks', json=data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['title'] == 'Tarea de prueba'
    assert json_data['description'] == 'Descripción de prueba'
