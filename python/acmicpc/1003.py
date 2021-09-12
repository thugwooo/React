T = int(input())
fibo = [[0,0] for _ in range(41)]
fibo[0] =[1,0]
fibo[1] = [0,1]
while T:
    n = int(input())
    if fibo[n] != [0,0]:
        print(fibo[n][0], fibo[n][1])
    else:
        for i in range(2,n+1):
            fibo[i][0] = fibo[i-1][0] +fibo[i-2][0]
            fibo[i][1] = fibo[i-1][1] +fibo[i-2][1]
        print(fibo[n][0], fibo[n][1])
    T-=1
