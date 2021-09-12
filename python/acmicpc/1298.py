import sys
n,m = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
maxv = 0
def dfs(depth):
    if depth == n:
        return 
    
