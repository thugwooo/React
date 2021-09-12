from collections import deque
n = int(input())

arr = [int(x) for x in range(1,n+1)]
arr = deque(arr)
while len(arr)>1:
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])