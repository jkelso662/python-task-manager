import pytest
from main import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_home(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == "Hello, Flask!"

def test_create_task(client):
    task = {'name': 'Test Task', 'done': True}
    rv = client.post('/tasks', json=task)
    json_data = rv.get_json()
    assert rv.status_code == 201
    assert json_data['name'] == task['name']
    assert json_data['done'] == task['done']

def test_get_tasks(client):
    task = {'name': 'Create repository', 'done': True}
    client.post('/tasks', json=task)
    rv = client.get('/get-tasks')
    json_data = rv.get_json()
    assert rv.status_code == 201
    assert len(json_data) > 0
    assert json_data[0][0] == task['name']
    assert json_data[0][1] == task['done']