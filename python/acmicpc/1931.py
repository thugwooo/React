import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr = sorted(arr,key=lambda x: (x[1],x[0]))

cnt = 0
start = 0

for a in arr:
    if a[0] >= start:
        start = a[1]
        cnt += 1
print(cnt)