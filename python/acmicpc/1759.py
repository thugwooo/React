l, c = map(int, input().split())
arr = sorted(input().split())
res = []
def dfs(index):
    if len(res) == l:
        cnt1 = 0
        cnt2 = 0
        for ch in res:
            if ch in ['a','e','i','o','u']:
                cnt1+=1
            else:
                cnt2+=1
            if cnt1>=1 and cnt2>=2:
                print("".join(map(str,res)))
                break
        return 
    for i in range(index,c):
        res.append(arr[i])
        dfs(i+1)
        res.pop()

dfs(0)