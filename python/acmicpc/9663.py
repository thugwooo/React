n = int(input())
cnt = 0
arr = []
def sol(depth):
    global cnt
    
    for i in range(len(arr)-1):
        if depth-1-i== abs(arr[depth-1]-arr[i]):
            return

    for i in range(n):
        if i in arr:
            continue
        else :
            arr.append(i)
            sol(depth+1)
            arr.pop()
    if depth==n:
        cnt+=1
        return 

sol(0)
print(cnt)
"""
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])== abs(i-j):
                return 
"""
    