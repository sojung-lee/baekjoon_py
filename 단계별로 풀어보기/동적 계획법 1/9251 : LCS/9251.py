a = list(str(input()))
b = list(str(input()))

arr = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
ans = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            arr[j+1][i+1] = arr[j][i] + 1
            ans = max(ans,arr[j+1][i+1])
        else:
            arr[j+1][i+1] = max(arr[j][i+1],arr[j+1][i])

print(ans)