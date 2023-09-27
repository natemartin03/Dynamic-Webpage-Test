from webapp.app import app
import pytest
from datetime import datetime

#checks date page
def test_date_page(client):
    response = client.get('/date')
    print(response.data)
    assert b"Current Date" in response.data
    
    # Check if date is accurate
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d").encode()
    assert current_date in response.data

#checks time page
def test_time_page(client):
    response = client.get('/time')
    print(response.data)
    assert b"Current Time" in response.data
    
    # Check if time is accurate
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").encode()
    assert current_time in response.data

#checks ampm page
def test_ampm_page(client):
    response = client.get('/ampm')
    print(response.data)
    assert b"AM/PM" in response.data
    
    # Check if ampm is accurate
    now = datetime.now()
    am_pm = "AM" if now.hour < 12 else "PM"
    assert am_pm.encode() in response.data
