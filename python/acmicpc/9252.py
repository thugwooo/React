arr1 = input()
arr2 = input()

a1 = len(arr1)
a2 = len(arr2)
mat = [[""] * (a2+1) for _ in range(a1+1)]

for i in range(1, a1+1):
    for j in range(1, a2+1):
        if arr1[i-1] == arr2[j-1]:
            mat[i][j] = mat[i-1][j-1]+arr1[i-1]
        else:
            if len(mat[i][j-1]) < len(mat[i-1][j]):
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i][j-1]

print(len(mat[a1][a2]))
if len(mat[a1][a2]):
    print(mat[a1][a2])