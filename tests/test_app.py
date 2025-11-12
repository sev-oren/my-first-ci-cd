"""Unit tests for Flask application."""
import pytest  # noqa: F401
from app import app


def test_hello_world():
    """Test main page response."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data
