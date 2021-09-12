def sol():
    n = int(input())
    k = 10000000
    arr = []
    for _ in range(n):
        a,b = [int(x)+k for x in input().split()]
        arr.append(a + b*k*2)
    arr.sort()
    for i in range(n):
        print(arr[i] % (2*k)-k,arr[i]//(2*k) -k)
sol()