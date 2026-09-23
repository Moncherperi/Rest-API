import requests

import pytest

@pytest.fixture
def base_url():
    return "https://postman-echo.com"

# Пишем первый тест - проверка GET запроса c query-параметрами

def test_get_request(base_url):
    url = f"{base_url}/get"
    payload = {"text": "hello"}
    response = requests.get(url, params=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["args"]["text"] == "hello"

# Проверка POST-запроса с передачей тела в формате JSON

def test_post(base_url):
    url = f"{base_url}/post"
    payload = {"text": "hello"}
    response = requests.post(url, json=payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["json"]["text"] == "hello"

# Проверка POST-запроса с отправкой данных в формате веб-формы

def test_post_form(base_url):
    url = f"{base_url}/post"
    payload = {"text": "hello"}
    response = requests.post(url, data=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["form"]["text"] == "hello"


# Проверка PUT-запроса для обновления данных в формате веб-формы

def test_put_form(base_url):
    url = f"{base_url}/put"
    payload = {"text": "hello"}
    response = requests.put(url, data=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["form"]["text"] == "hello"

# Проверка DELETE-запроса без передачи тела (удаление ресурса)

def test_delete_request(base_url):
    url = f"{base_url}/delete"
    response = requests.delete(url)
    response_json = response.json()

    assert response.status_code == 200
