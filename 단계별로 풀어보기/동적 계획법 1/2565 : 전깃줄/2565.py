n = int(input())
arr = []
for i in range(n):
    a, b = map(int,input().split())
    arr.append([a,b])

arr = sorted(arr, key = lambda x: x[0])

dp = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[i].append(arr[i][1])
    else:
        for j in range(0,i):
            if dp[j][-1] < arr[i][1]:
                if len(dp[i])-1 < len(dp[j]):
                    dp[i] = dp[j] + [arr[i][1]]
        if not dp[i]:
            dp[i].append(arr[i][1])

max_num = 0
for i in range(n):
    max_num = max(max_num, len(dp[i]))
print(n - max_num)

