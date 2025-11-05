from app import app

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data

def test_hello_world_with_id():
    with app.test_client() as client:
        response = client.get('/?id=42')
        assert response.status_code == 200
        assert b'user #42' in response.data

def test_health_check():
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert b'OK' in response.data
