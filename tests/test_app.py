import requests


def test_create_task():
    url = 'http://localhost:5000/tasks'
    data = {
        'title': 'Tarea 1',
        'description': 'Descripción de la tarea 1'
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201, \
        f"Expected 201, got {response.status_code}"
    assert response.json()['title'] == data['title'], "Title does not match"
    assert response.json()['description'] == data['description'], \
        "Description does not match"


def test_get_tasks():
    url = 'http://localhost:5000/tasks'
    response = requests.get(url)
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response is not a list"


def test_create_task_missing_title():
    url = 'http://localhost:5000/tasks'
    data = {
        'description': 'Tarea sin título'
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}"
    assert response.json()['error'] == 'El título es obligatorio', \
        "Error message mismatch"


if __name__ == "__main__":
    test_create_task()
    test_get_tasks()
    test_create_task_missing_title()
    print("All tests passed!")
