n = int(input())
a = list(map(int, input().split()))
dpf = [0 for _ in range(n)]
dpb = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i]>a[j] and dpf[i]<dpf[j]:
            dpf[i] = dpf[j]
    dpf[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i]>a[j] and dpb[i]<dpb[j]:
            dpb[i] = dpb[j]
    dpb[i] += 1

for i in range(n):
    dp[i] = dpf[i] + dpb[i] -1
print(max(dp))

