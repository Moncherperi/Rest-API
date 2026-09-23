import requests

# Пишем первый тест - проверка GET запроса c query-параметрами

def test_get_request():
    url = "https://postman-echo.com/get"
    payload = {"text": "hello"}
    response = requests.get(url, params=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["args"]["text"] == "hello"

# Проверка POST-запроса с передачей тела в формате JSON

def test_post():
    url = "https://postman-echo.com/post"
    payload = {"text": "hello"}
    response = requests.post(url, json=payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["json"]["text"] == "hello"

# Проверка POST-запроса с отправкой данных в формате веб-формы

def test_post_form():
    url = "https://postman-echo.com/post"
    payload = {"text": "hello"}
    response = requests.post(url, data=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["form"]["text"] == "hello"


# Проверка PUT-запроса для обновления данных в формате веб-формы

def test_put_form():
    url = "https://postman-echo.com/put"
    payload = {"text": "hello"}
    response = requests.put(url, data=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["form"]["text"] == "hello"

# Проверка DELETE-запроса без передачи тела (удаление ресурса)

def test_delete_request():
    url = "https://postman-echo.com/delete"
    response = requests.delete(url)
    response_json = response.json()

    assert response.status_code == 404
