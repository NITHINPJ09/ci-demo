from functions import add, subtract, multiply, divide
from functions import convert_fahrenheit_to_celsius as f2c
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def test_subtract():
    assert subtract(2, 3) == -1
    
def test_multiply():
    assert multiply(2, 3) == 6
    
def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ZeroDivisionError):
        divide(6, 2)

def test_convert_fahrenheit_to_celsius():
    assert f2c(32) == 0
    assert f2c(122) == pytest.approx(50)
