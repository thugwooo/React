n = int(input())
arr = [[0 for i in range(10)] for i in range(n+1)]
arr[1] = [1,1,1,1,1,1,1,1,1]
for i in range(2,n):
    s = 0
    for j in range(9,-1,-1):
        print(j)
        s += arr[i-1][j]
        arr[i][j] = s
        
sumv = 0
print(arr)
for i in range(n):
    sumv += sum(arr[i])