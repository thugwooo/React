arr = [1,1,2,2,3,4,5,6,9,12]
def sol():
    t = int(input())
    value = 0
    arr = []
    for _ in range(t):
        a = int(input())
        arr.append(a)
        value = max(value,a)
    rst = [1,1,1,2,2]
    for i in range(5,value):
        tmp = rst[i-1] + rst[i-5]
        rst.append(tmp)
    for i in range(t):
        print(rst[arr[i]-1])

sol()
