n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

sum = distance[0]*price[0]
value = price[0]
for i in range(1, n-1):
    value = min(price[i],value)
    sum += distance[i]*value
    
print(sum)