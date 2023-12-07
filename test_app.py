from fastapi import FastAPI
from fastapi.testclient import TestClient

from  fastapi_ex import pe_urfu



client = TestClient(pe_urfu)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_read_api():
    response = client.get("/api")
    assert response.status_code == 200

def test_read_api():
    response = client.get("/api")
    assert response.status_code == 200

def test_read_api_image_get():
    response = client.get("/api/image/get")
    assert response.status_code == 404


def test_read_api_images():
    response = client.get("/api/images")
    assert response.status_code == 200

