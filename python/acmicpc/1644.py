n = int(input())

a = [False, False] + [True] * (n-1)
prime= []

for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
        
start, end = 0,1
cnt = 0
s = [0]
for i in range(len(prime)):
    s.append(s[i]+prime[i])

while start<len(s) and end<len(s):
    tmp = s[end] - s[start]
    if tmp == n:
        cnt+=1
        start+=1
    elif tmp>n:
        start+=1
    else:
        if end<len(s)-1:
            end+=1
        else:
            start+=1

print(cnt)

