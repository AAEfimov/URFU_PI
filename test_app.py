"""
test_app.py
Tests for fastapi wrappers.
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2023, Planet Earth"


from fastapi import FastAPI
from fastapi.testclient import TestClient
from jsonschema import validate

from fastapi_ex import pe_urfu

client = TestClient(pe_urfu)


def test_read_root():
    """
    Test root page.
    only status code == 200
    """
    response = client.get("/")
    assert response.status_code == 200


def test_read_api():
    """
    test API page
    """
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Добро пожаловать в API для генератора изображений"
    }


def test_read_api_image_get():
    """
    Test 404. Try to load non-existent image
    """
    response = client.get("/api/image/get/123")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_read_api_images():
    """
    Test correct JSON schema for existen response
    """
    response = client.get("/api/images")
    assert response.status_code == 200
    schema_str = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "pwd": {"type": "string"},
            "test": {"type": "string"},
            "img_id": {"type": "string"},
        },
    }
    if len(response.json()):
        for v in response.json():
            validate(v, schema_str)
    else:
        assert response.json() == []
