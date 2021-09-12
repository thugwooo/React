t = int(input())
for _ in range(t):
    a,b = input().split()
    print(a,'&',b,'are',end=' ')
    if sorted(a) != sorted(b):
        print("NOT",end=' ')
    print("anagrams.")
