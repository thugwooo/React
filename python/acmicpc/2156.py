n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = arr[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]
print(max(dp[n-1]))


