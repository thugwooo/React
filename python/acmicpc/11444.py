def power(arr,n):
    if n==1:
        return arr
    elif n%2:
        return multi(power(arr,n-1), arr)
    else:
        return power(multi(arr,arr), n//2)

def multi(a,b):
    tmp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum+= a[i][k]*b[k][j]
            tmp[i][j]=sum%1000000007
    return tmp


n  = int(input())
arr = [[1,1],[1,0]]
start = [[1],[1]]

if n<3:
    print(1)
else:
    print(multi(power(arr,n-2),start)[0][0])


#https://www.acmicpc.net/blog/view/28