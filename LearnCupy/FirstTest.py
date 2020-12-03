import cupy as cp
import numpy as np

import math
import matplotlib.pyplot as plt


array1 = cp.array([1, 7, 5, 6, 9])
array2 = cp.array([2, 4, 9, 1, 1])


x = cp.linspace(-math.pi, math.pi, 100)             # mathplotlib dosnt work with cupy
f = cp.cos(x)

x = cp.asnumpy(x)
f = cp.asnumpy(f)


if __name__ == '__main__':
    plt.plot(x, f)
    plt.show()
    print(array1 + array2)
