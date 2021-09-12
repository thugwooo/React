import sys
n = int(input())
arr = sorted([int(x) for x in sys.stdin.readline().split()])

start, end = 0, n-1
res = arr[start]+arr[end]
ast = start
ae = end

while start<end:
    tmp = arr[start]+arr[end]
    if abs(tmp) < abs(res):
        ast=start
        ae = end
        res = tmp
        if res == 0:
            ast, ae = start, end
            break

    if tmp < 0:
        start +=1
    else :
        end-=1
print(arr[ast],arr[ae])

