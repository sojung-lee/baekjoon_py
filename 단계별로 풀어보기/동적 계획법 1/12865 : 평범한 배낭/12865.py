import sys

n, k = map(int,sys.stdin.readline().split())
item = [[0,0]]
for i in range(1, n+1):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j>=item[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]]+item[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
