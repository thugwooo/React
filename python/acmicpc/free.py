a, b, v = map(int, input().split())

day = 0
c = 0
while True: 
    day +=1
    c += a
    if c>=v:
        break
    c -= b
    print(day)
print(day)

