import numpy as np

def sol():
    n, b = [int(x) for x in input().split()]
    mat = []
    for _ in range(n):
        tmp = [int(x) for x in input().split()]
        mat.append(tmp)
        mat1 = np.reshape(mat,(n,n))
