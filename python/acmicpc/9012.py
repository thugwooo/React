def sol():  
    data = input()
    arr = []
    for item in data:
        if item =='(':
            arr.append(item)
        else:
            if len(arr) ==0:
                print("NO")
                return
            arr.pop()
    if len(arr) == 0:
        print("YES")
    else:
        print("NO")
n = int(input())
for _ in range(n):
    sol()