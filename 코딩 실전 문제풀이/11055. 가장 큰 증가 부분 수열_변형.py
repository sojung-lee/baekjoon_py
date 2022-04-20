import copy
N, A = int(input()), list(map(int, input().split()))
idx = 0
DP = copy.deepcopy(A)
rev = [i for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and DP[i] < A[i] + DP[j]:
            DP[i] = A[i] + DP[j]
            rev[i] = j
    if DP[idx] < DP[i]:
        idx = i

print(idx, DP[idx])
print(rev)
print(DP)
print(max(DP))

while rev[idx] != idx:
    print(A[idx], sep=' ')
    idx = rev[idx]

print(A[idx])