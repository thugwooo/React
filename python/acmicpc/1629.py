a,b,c = map(int,input().split())

def pow(a,b):
    if b==0:
        return 1
    elif b%2==0:
        n = pow(a,b/2)
        return (n*n)%c
    else:
        n = pow(a,(b-1)/2)
        return (a*n*n)%c

print(pow(a,b)%c)