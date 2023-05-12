from app import app

def test_client():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
