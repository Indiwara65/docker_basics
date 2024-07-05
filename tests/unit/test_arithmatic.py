from arithmatic_package import arithmatic
import pytest

def test_add():
    assert arithmatic.add(10,5) == 15
    assert arithmatic.add(10.5,3.25) == 13.75
    assert arithmatic.add(11.25,3.25) == 14.5
    assert arithmatic.add(10,0.25) == 10.25

def test_substract():
    assert arithmatic.substract(10,5) == 5
    assert arithmatic.substract(10.5,3.25) == 7.25
    assert arithmatic.substract(11.25,16) == -4.75
    assert arithmatic.substract(10,11.25) == -1.25

def test_multiply():
    assert arithmatic.multiply(10,5) == 50
    assert arithmatic.multiply(10.5,3.25) == 34.125
    assert arithmatic.multiply(11.25,3.25) == 36.5625
    assert arithmatic.multiply(10,0.25) == 2.5

def test_divide():
    assert arithmatic.divide(10,5) == 2
    assert arithmatic.divide(10,2.5) == 4
    assert arithmatic.divide(24,8) == 3
    assert arithmatic.divide(32,27) == pytest.approx(1.185185)
    with pytest.raises(ZeroDivisionError):
        arithmatic.divide(10, 0)
