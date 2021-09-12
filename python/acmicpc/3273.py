import sys
n = int(input())
arr = sorted([int(x) for x in sys.stdin.readline().split()])
x = int(input())
cnt = 0
start,end=0,n-1
while start<end:
    tmp = arr[start]+arr[end]
    if tmp == x:
        cnt+=1
    if tmp<x:
        start+=1
        continue
    end-=1
print(cnt)