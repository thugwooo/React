import sys
import math
from collections import Counter
n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
print(math.ceil(sum(arr)/n))
arr.sort()
print(arr[n//2])
asdf = Counter(arr).most_common()
print(asdf[0][0])
print(max(arr)-min(arr))