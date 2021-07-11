n,m = map(int, input().split())
visited = [0 for _ in range(n)]
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]==1
            arr.append(i+1)

            dfs(cnt+1)
            visited[i] = 0
            arr.pop()

dfs(0)


