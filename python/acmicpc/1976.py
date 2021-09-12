def find(i, rst):
    if rst[i] != i:
        rst[i] = find(rst[i],rst)
    
    return rst[i]
def union(i,j,rst):
    x = find(i, rst)
    y = find(j, rst)
    rst[x] = y
def sol():
    n = int(input())
    m = int(input())
    arr = []
    for _ in range(n):
        tmp = [int(x) for x in input().split()]
        arr.append(tmp)
    test = [int(x) - 1 for x in input().split()]
    rst = list(range(n))
    for i in range(n):
        for j in range(i+1,n):
            if arr[i][j] == 1:
                union(i,j,rst)
    pivot = find(test[0], rst)
    for i in range(1, m):
        if pivot != find(test[i], rst):
            print("NO")
            return
        
    print("YES")

sol()