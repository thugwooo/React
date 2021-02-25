N = 20001
def sol():
    n = int(input())
    arr =[set() for _ in range(N)]
    for _ in range(n):
        a = input()
        arr[len(a)].add(a)
        
    
    for i in range(N):
        for item in sorted(arr[i]):
            print(item)
sol()