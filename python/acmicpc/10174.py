t = int(input())
for _ in range(t):
    words = input().lower()
    if words==words[::-1]:
        print("Yes")
    else:
        print("No")