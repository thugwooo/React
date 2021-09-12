import sys
N,B=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def matric_mul(A,B):
    if B==1:
        for i in range(N):
            for j in range(N):
                A[i][j]%=1000
        return A

    elif B%2==1:
        tmp=[[0 for _ in range(N)] for _ in range(N)]
        C=matric_mul(A,B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*A[k][j]
                tmp[i][j]%=1000

        return tmp

    else:
        tmp=[[0 for _ in range(N)] for _ in range(N)]
        C=matric_mul(A,B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*C[k][j]
                tmp[i][j]%=1000
        return tmp

result=matric_mul(A,B)
for li in result:
    for p in li:
        print(p,end=' ')
    print()




"""import sys
def mul(n,mat1,mat2):
    rst = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                rst[i][j] += mat1[i][k] * mat2[k][j]
            rst[i][j] %1000
    
    return rst

def div(n, b, mat):
    if b==1:
        return mat
    elif b==2:
        return mul(n, mat,mat)
    else:
        tmp = div(n,b//2,mat)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),mat)

n, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rst = div(n, b, arr)
for row in rst:
    for num in row:
        print(num%1000, end=' ')
    print()

"""