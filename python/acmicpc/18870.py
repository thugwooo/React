import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

sar = sorted(list(set(arr)))

answer = []
for i in arr:
    answer.append(sar.index(i))
print(" ".join(map(str,answer)))