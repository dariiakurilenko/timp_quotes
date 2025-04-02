import pytest
from app import app, quotes
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Проверяет, что главная страница возвращает статус 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_get_quote(client):
    """Проверяет, что GET /quote возвращает случайную цитату."""
    response = client.get('/quote')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'quote' in data
    assert data['quote'] in quotes

def test_add_quote(client):
    """Проверяет добавление новой цитаты через POST /quote."""
    new_quote = "Новая тестовая цитата."
    response = client.post(
        '/quote',
        data=json.dumps({'quote': new_quote}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == "Цитата добавлена!"
    assert data['quote'] == new_quote
    assert new_quote in quotes

def test_add_quote_empty(client):
    """Проверяет обработку ошибки при отсутствии цитаты."""
    response = client.post(
        '/quote',
        data=json.dumps({}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['error'] == "Цитата отсутствует."