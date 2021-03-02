N = 100000
def sol():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = [int(x) + N for x in input().split()]
        tmp = a * 2 *N + b
        arr.append(tmp)
    arr.sort()
    for item in arr:
        print(item//(2*N) - N, item % (2*N) - N)

sol()
