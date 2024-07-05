from arithmatic_package import numpy_arithmatic
import pytest
import numpy as np

@pytest.fixture
def init():
    a = np.array([3, 4, 5])
    b = np.array([-2, -5, -10])
    c = np.expand_dims(a, axis=0)
    d = np.array([1, 2, 3, 4])
    return a, b, c, d

def test_numpy_add(init):
    a, b, c, d = init
    assert np.array_equal(numpy_arithmatic.add(a, b), np.array([1, -1, -5]))
    with pytest.raises(NotImplementedError):
        numpy_arithmatic.add(a, c)
    with pytest.raises(ValueError):
        numpy_arithmatic.add(a, d)

def test_numpy_substract(init):
    a, b, c, d = init
    assert np.array_equal(numpy_arithmatic.substract(a, b), np.array([5, 9, 15]))
    with pytest.raises(NotImplementedError):
        numpy_arithmatic.substract(a, c)
    with pytest.raises(ValueError):
        numpy_arithmatic.substract(a, d)

def test_numpy_multiply(init):
    a, b, c, d = init
    assert np.array_equal(numpy_arithmatic.multiply(a, b), np.array([-6, -20, -50]))
    with pytest.raises(NotImplementedError):
        numpy_arithmatic.multiply(a, c)
    with pytest.raises(ValueError):
        numpy_arithmatic.multiply(a, d)

def test_numpy_divide(init):
    a, b, c, d = init
    e = np.array([1, 1, 0])
    f = np.array([1, 0, 0])
    g = np.array([0, 0, 0])
    assert np.allclose(numpy_arithmatic.divide(a, b), np.array([-1.5, -0.8, -0.5]))
    with pytest.raises(NotImplementedError):
        numpy_arithmatic.divide(a, c)
    with pytest.raises(ValueError):
        numpy_arithmatic.divide(a, d)
    with pytest.raises(ZeroDivisionError):
        numpy_arithmatic.divide(a, e)
    with pytest.raises(ZeroDivisionError):
        numpy_arithmatic.divide(a, f)
    with pytest.raises(ZeroDivisionError):
        numpy_arithmatic.divide(a, g)

