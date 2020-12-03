import cupy as cp
import numpy as np

import math
import matplotlib.pyplot as plt


def bwd_subs(U, y):
    """Solve the linear system Ux = y with upper triangular matrix U by backward substitution."""

    n = y.size

    out = cp.array([y[0, n - 1] / U[n - 1, n - 1]]).reshape((1, 1))

    for row in range(U.shape[1] - 2, -1, -1):
        new_out = cp.array((y[0, row] - cp.sum(U[row, row + 1] * out)) / U[row, row]).reshape((1, 1))
        print(new_out.shape)
        print(out.shape)
        out = cp.concatenate(out, new_out)

    return out

    # if n == U.shape[0]:
    #     return cp.array()
    # else:
    #     return cp.concatenate(cp.array([(y[n] - cp.sum(U[n, n + 1] * bwd_subs(U, y[:-1])) ) / U[n, n]]), bwd_subs(U, y[:-1]))


def gauss_solve(A, b):
    """Solve the linear system Ax=b using direct Gaussian elimination and backward substitution."""

    # TO DO

    return None


if __name__ == '__main__':
    U = cp.array([[6, 6, -12],
                  [0, 24, -42],
                  [0, 0, -258]])
    y = cp.array([42, 114, 258]).reshape((1, 3))
    print(bwd_subs(U, y))
