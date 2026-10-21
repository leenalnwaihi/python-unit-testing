from main import add, divide, get_weather
import pytest

def test_get_weather():
    assert get_weather(25) == "hot"
    assert get_weather(15) == "cold"

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError , match="Cannot divide by zero"):
        divide(10, 0)