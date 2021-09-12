n, k = map(int,input().split())

arr = [[0] *(n+1) for _ in range(k+1)]

arr[0][0] = 1
for i in range(1,k+1):
    for j in range(n+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        arr[i][j] %= 1000000000
print(arr[k][n])