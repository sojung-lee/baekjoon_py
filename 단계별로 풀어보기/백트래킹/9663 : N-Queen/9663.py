n = int(input())
arr = [0 for i in range(16)]
result = 0

def isTrue(x):
    for i in range(1,x):
        if arr[x] == arr[i] or abs(arr[x]-arr[i]) == x - i: #열 or 대각선 같을 때
            return False
    return True

def dfs(cnt):
    global result
    if cnt>n:
        result += 1
    else:
        for i in range(1,n+1):
            arr[cnt] = i
            if isTrue(cnt):
                dfs(cnt+1)

dfs(1)
print(result)