n, m = map(int,input().split())
arr = sorted([int(x) for x in input().split()])
res = []
def dfs():
    if len(res) == m:
        print(" ".join(map(str,res)))
        return
    for i in arr:
        res.append(i)
        dfs()
        res.pop()
dfs()