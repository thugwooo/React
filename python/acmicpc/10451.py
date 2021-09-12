def asdf(start):
    if arr[start] == start:
        res +=1
        return
    if arr[start] and arr[start] not in visited:
        visited.append(arr[start])
        return asdf(arr[start]) 


t = int(input())
while t:
    t-=1
    res = 0
    visited = []
    arr = []
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        asdf(i)
    print(res)
