from arithmatic_package import arithmatic
from arithmatic_package import numpy_arithmatic
import numpy as np


def main():
    a = 10
    b = 12.3
    print("arithmatic module")
    print(f"{a}+{b}={arithmatic.add(a, b)}")
    print(f"{a}-{b}={arithmatic.substract(a, b)}")
    print(f"{a}x{b}={arithmatic.multiply(a, b)}")
    print(f"{a}/{b}={arithmatic.divide(a, b)}\n")

    a = np.array([1, 2, 3])
    b = -a
    print("numpy_arithmatic module")
    print(f"{a}+{b}={numpy_arithmatic.add(a, b)}")
    print(f"{a}-{b}={numpy_arithmatic.substract(a, b)}")
    print(f"{a}x{b}={numpy_arithmatic.multiply(a, b)}")
    print(f"{a}/{b}={numpy_arithmatic.divide(a, b)}")


if __name__ == "__main__":
    main()
