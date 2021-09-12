n,m = map(int,input().split())
arr = sorted([int(x) for x in input().split()])
res = []

def dfs(k):
    if len(res) == m:
        print(" ".join(map(str,res)))
        return
    for i in range(k,n):
        res.append(arr[i])
        dfs(i)
        res.pop()
dfs(0)