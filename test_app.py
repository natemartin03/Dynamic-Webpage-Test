import pytest
from app import app

#Creates test client
@pytest.fixture
def client():
    return app.test_client()

#Tests date page
def test_date_page(client):
    response = client.get("/date")
    assert response.status_code == 200  #A response status code of 200 is good

#Tests time page
def test_time_page(client):
    response = client.get("/time")
    assert response.status_code == 200

#Tests ampm page
def test_ampm_page(client):
    response = client.get("/ampm")
    assert response.status_code == 200