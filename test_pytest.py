'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"
