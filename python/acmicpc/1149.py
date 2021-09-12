def sol():
    n = int(input())
    rst = []
    for i in range(n):
        rst.append(list(map(int,input().split())))

    for i in range(1,n):
        rst[i][0] = min(rst[i-1][1], rst[i-1][2]) + rst[i][0]
        rst[i][1] = min(rst[i-1][0], rst[i-1][2]) + rst[i][1]
        rst[i][2] = min(rst[i-1][0], rst[i-1][1]) + rst[i][2]

    print(min(rst[n-1][0], rst[n-1][1], rst[n-1][2]))

sol()