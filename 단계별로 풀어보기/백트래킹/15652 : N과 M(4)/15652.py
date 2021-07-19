import sys
n, m = map(int, input().split())
visited = [0 for _ in range(n)]
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i] == 0:
            arr.append(i+1)
            dfs(cnt+1)
            visited[i]=1
            arr.pop()

            for j in range(i+1,n):
                visited[j]=0
dfs(0)