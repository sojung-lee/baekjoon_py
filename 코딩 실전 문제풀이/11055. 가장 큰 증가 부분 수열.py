import copy
N, A = int(input()), list(map(int, input().split()))

DP = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i] + DP[j], DP[i])

#print(DP)
print(max(DP))
