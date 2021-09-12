k, n = map(int,input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
right = max(arr)
left = 1

while left<=right:

    sum = 0
    mid = (right+left)//2
    for v in arr:
        sum += v//mid
    
    if sum>=n:
        left = mid +1
    else :
        right = mid -1

print(right)
