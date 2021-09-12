def sol():
    N = int(input())
    x = []
    y = []
    cnt = [1 for _ in range(N)]
    for _ in range(N):
        m,n = map(int,input().split())
        x.append(m)
        y.append(n)
    for i in range(N):
        for j in range(N):
            if x[i]<x[j] and y[i]<y[j]:
                cnt[i] +=1
    for i in range(N):
        print(cnt[i], end=" ")

        

sol()