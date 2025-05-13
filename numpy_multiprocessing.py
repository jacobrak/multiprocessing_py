import numpy as np
from multiprocessing import Pool

def matrix_mult(args):
    a, b = args
    return np.dot(a, b)


if __name__ == '__main__':
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    c = np.random.rand(1000, 1000)
    d = np.random.rand(1000, 1000)

    with Pool(4) as pool:
        results = pool.map(matrix_mult, [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)])

    print(results)