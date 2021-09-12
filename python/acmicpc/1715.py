import sys
import heapq

N = int(input())
card = [int(sys.stdin.readline()) for _ in range(N)]

heapq.heapify(card)
result = 0

while len(card) is not 1:
    s = 0
    
    for i in range(2):
        s += heapq.heappop(card)
    
    result += s
    heapq.heappush(card, s)
    
print(result)


from queue import PriorityQueue

n = int(input())
q = PriorityQueue()
result = 0

for i in range(n):
    q.put(int(input()))

while q.qsize() >=2:
    a = q.get()
    b = q.get()
    result += a+b
    q.put(a+b)
print(result)