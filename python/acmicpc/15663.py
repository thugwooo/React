n, m = map(int,input().split())

arr = sorted([int(x) for x in input().split()])

res = []
ress = []
def dfs(k):
    if len(res) == m:
        
        if res not in ress:
            ress.append(res)
            print(ress)
            print(" ".join(map(str, res)))
        return
    for i in arr:
        if i==k and i !=0:
            continue
        res.append(i)
        dfs(i)
        res.pop()
dfs(0)