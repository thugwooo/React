n,m = map(int, input().split())
arr =[]

def sol(num):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return

    for i in range(num, n+1):
        arr.append(i)
        sol(i)
        arr.pop()

sol(1)