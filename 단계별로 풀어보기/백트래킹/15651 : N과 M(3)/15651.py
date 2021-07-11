n,m = map(int,input().split())
arr = []

def dfs(cnt):
    if cnt==m:
        print(*arr)
        return

    for i in range(n):
        arr.append(i+1)
        dfs(cnt+1)
        arr.pop()

dfs(0)