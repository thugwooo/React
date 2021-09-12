n, k = map(int,input().split())
arr = []
cnt = 0
for _ in range(n):
    arr.append(int(input()))
arr = arr[::-1]
for i in arr:
    cnt += k//i
    k %=i
print(cnt)