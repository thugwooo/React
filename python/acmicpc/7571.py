n, m = map(int, input().split())
x = []
y = []
for _ in range(m):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
res = 0
for i in range(m):
    res += abs(x[m//2]-x[i]) + abs(y[m//2]-y[i])

print(res)
