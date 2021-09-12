import sys

n,m = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split()))
s = [0]
for i in range(n):
    s.append(arr[i]+s[i])
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    print(s[b]-s[a-1])