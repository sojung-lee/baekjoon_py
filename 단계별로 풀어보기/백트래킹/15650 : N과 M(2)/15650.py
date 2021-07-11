import sys
read = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
check_list = [False]*n

arr = []
def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if check_list[i]:
            continue
        check_list[i] = True
        arr.append(lst[i])
        dfs(cnt+1)
        arr.pop()

        for j in range(i+1, n):
            check_list[j] = False
dfs(0)