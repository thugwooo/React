import sys
n, c = map(int, input().split())

arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    arr.append(x)

arr.sort()

start = 1
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start+end)//2
    ans = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= ans + mid:
            cnt+=1
            ans = arr[i]
    
    if cnt >=c:
        start = mid+1
        res = mid
    else:
        end = mid-1

print(res)