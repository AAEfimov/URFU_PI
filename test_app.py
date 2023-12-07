from fastapi import FastAPI
from fastapi.testclient import TestClient

from  fastapi_ex import pe_urfu



client = TestClient(pe_urfu)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    
