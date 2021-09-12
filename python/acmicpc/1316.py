def sol():
    n = int(input())
    cnt = 0
    for _ in range(n):
        word = input()
        cnt +=list(word) == sorted(word, key=word.find)

    print(cnt)

sol()