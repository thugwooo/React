
arr1 = input()
arr2 = input()
a1 = len(arr1)
a2 = len(arr2)
matrix = [[0] *(a2+1) for _ in range(a1+1)]

for i in range(1, a1+1):
    for j in range(1, a2+1):
        if arr1[i-1] == arr2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])