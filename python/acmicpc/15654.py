n, m = map(int,input().split())
arr = sorted([int(x) for x in input().split()])

res = []

def dfs(i):
    if len(res) == m:
        print(" ".join(map(str, res)))
        return
    for i in range(i,n):
        if arr[i] in res:
            continue
        res.append(arr[i])
        dfs(i+1)
        res.pop()

dfs(0)