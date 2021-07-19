import sys
input = sys.stdin.readline
num = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -1000000001
min_result = 1000000001

def dfs(cnt, result, add, sub, mul, div):
    global max_result
    global min_result
    if cnt == num:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if add:
        dfs(cnt+1, result + number[cnt], add-1, sub, mul, div)
    if sub:
        dfs(cnt+1, result - number[cnt], add, sub-1, mul, div)
    if mul:
        dfs(cnt+1, result * number[cnt], add, sub, mul-1, div)
    if div:
        dfs(cnt+1, -(-result // number[cnt]) if result<0 else result//number[cnt], add, sub, mul, div-1)

dfs(1, number[0], add, sub, mul, div)
print(max_result)
print(min_result)