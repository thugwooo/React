def sol():
    n = int(input())
    answer = 0
    for i in range(1, n):
        a = list(map(int, str(i)))
        answer = i + sum(a)
        if answer == n:
            print(i)
            break
    if i==n:
        print(0)
sol()