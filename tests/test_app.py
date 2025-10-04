import pytest
import sys
import os
# Добавляем корневую директорию в Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app
def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data
