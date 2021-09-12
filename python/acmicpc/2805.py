import sys
n,m = map(int,input().split())

arr = [int(x) for x in sys.stdin.readline().split()]

left = 1
right = max(arr)
while left<=right:
    sum = 0
    mid = (left + right)//2
    for v in arr:
        if v - mid >0:
            sum+=(v-mid)
    if sum>=m:
        left = mid+1
    else :
        right = mid-1
    
print(right)