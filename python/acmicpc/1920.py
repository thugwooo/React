import sys
n = int(sys.stdin.readline())
arr1 = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
arr2 = [int(x) for x in sys.stdin.readline().split()]
answer = []
arr1 = set(arr1)
for i in arr2:
    if i in arr1:
        answer.append(1)
    else:
        answer.append(0)

print("\n".join(map(str,answer)))

#set 의 in은 시간복잡도가 O(1)이다. 
#다른 풀이로는 이진탐색정도?

"""
import sys 
def bin(left, right, x):
    print(left, right)
    if left > right:
        return 0
    
    mid = (left+right)//2
    if x == arr1[mid]:
        return 1
    elif arr1[mid] > x:
        return bin(left, mid-1, x)
    else:
        return bin(mid+1,right,x)

n = int(input())
arr1 = [int(x) for x in sys.stdin.readline().split()]
arr1.sort()
m = int(input())
arr2 = [int(x) for x in sys.stdin.readline().split()]
answer = [0] * m
for i,v in enumerate(arr2):
    answer[i] = bin(0,m-1,v)

print(answer)
"""