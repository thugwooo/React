t = int(input())
cnt= [0]*3
if t%10 !=0 :
    print("-1")
else :
    cnt[0] = t//300
    t %= 300
    cnt[1] = t//60
    t %= 60
    cnt[2] = t//10
    print(" ".join(map(str,cnt)) )