def sol():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(min(arr)*max(arr))

sol()