n = int(input())
arr = [int(input()) for i in range(n)]

dp = [0]
dp.append(arr[0])
if n>1:
    dp.append(arr[0]+arr[1])

for i in range(3, n+1):
    case1 = arr[i-1] + dp[i-2]
    case2 = arr[i-1] + arr[i-2] + dp[i-3]
    case3 = dp[i-1]
    max_value = max(case1,case2,case3)
    dp.append(max_value)

print(dp[n])