from http import HTTPStatus


def test_read_root_deve_retornar_ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'password',
            'email': 'testeemail@teste.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'id': 1,
        'email': 'testeemail@teste.com',
    }
def test_read_users(client):
    response =client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.JSON() == [
        {
            'username': 'testeusername',
            'id': 1,
            'email': 'testeemail@teste.com'
        }
    ]