n, m = map(int, input().split())
num = [int(x) for x in input().split()]
sum =0
rst = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = num[i] + num[j] + num[k]
            if sum <= m:
                rst = max(sum,rst)

print(rst)