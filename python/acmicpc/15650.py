n,m = map(int,input().split())
arr = []
def sol():
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                return

    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
        
    for i in range(1,n+1):
        if i in arr:
            continue
        
        arr.append(i)
        sol()
        arr.pop()

sol()