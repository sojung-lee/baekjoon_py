import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*100
dp[1] = 1
dp[2] = 1
dp[3] = 1
for j in range(n):
    num = int(input())
    for i in range(4,num+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[num])