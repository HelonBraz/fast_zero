from http import HTTPStatus
from textwrap import dedent

from fastapi.testclient import TestClient

from fast_zero.app import app


# def test_root_deve_retornar_ok_e_ola_mundo(client):
def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Aí dentro!'}


# def test_root_html_deve_retornar_ok_e_ola_mundo(client):
def test_root_html_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/exemplo/html')
    response_text_esperado = dedent("""
        <html>
            <head>
                <title> Nosso olá mundo!</title>
            </head>
            <body>
                <h1> Olá Mundo </h1>
            </body>
        </html>""")

    assert response.status_code == HTTPStatus.OK
    assert dedent(response.text) == response_text_esperado


# def test_create_user(client):
def test_create_user():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


# def test_read_users(client):
def test_read_users():
    client = TestClient(app)
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


# def test_update_user(client):
def test_update_user():
    client = TestClient(app)
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


# def test_delete_user(client):
def test_delete_user():
    client = TestClient(app)
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


if __name__ == '__main__':
    pass
