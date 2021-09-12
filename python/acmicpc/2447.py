n = int(input())

def sol(n):
    if n==1:
        print("\n")
        return
    print("***", end="")
    sol(n/3)
    print("* *",end="")
    sol(n/3)
    print("***",end="")
    sol(n/3)

sol(n)