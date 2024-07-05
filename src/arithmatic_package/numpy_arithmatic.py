import numpy as np


def add(x: np.ndarray, y: np.ndarray):
    if x.ndim != 1 or y.ndim != 1:
        raise NotImplementedError("Only implemented for 1D arrays")
    elif x.shape != y.shape:
        raise ValueError("The dimensions of the two arrays do not match.")
    else:
        z = np.empty(x.shape)
        for i in range(len(x)):
            z[i] = x[i] + y[i]
    return z


def substract(x: np.ndarray, y: np.ndarray):
    if x.ndim != 1 or y.ndim != 1:
        raise NotImplementedError("Only implemented for 1D arrays")
    elif x.shape != y.shape:
        raise ValueError("The dimensions of the two arrays do not match.")
    else:
        z = np.empty(x.shape)
        for i in range(len(x)):
            z[i] = x[i] - y[i]
    return z


def multiply(x: np.ndarray, y: np.ndarray):
    if x.ndim != 1 or y.ndim != 1:
        raise NotImplementedError("Only implemented for 1D arrays")
    elif x.shape != y.shape:
        raise ValueError("The dimensions of the two arrays do not match.")
    else:
        z = np.empty(x.shape)
        for i in range(len(x)):
            z[i] = x[i] * y[i]
    return z


def divide(x: np.ndarray, y: np.ndarray):
    if x.ndim != 1 or y.ndim != 1:
        raise NotImplementedError("Only implemented for 1D arrays")
    elif x.shape != y.shape:
        raise ValueError("The dimensions of the two arrays do not match.")
    elif 0 in y:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        z = np.empty(x.shape)
        for i in range(len(x)):
            z[i] = x[i] / y[i]
    return z
