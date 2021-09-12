n = int(input())
arr = sorted([int(x) for x in input().split()])

res = 1
for w in arr:
    if res < w:
        break
    res +=w
print(res)
