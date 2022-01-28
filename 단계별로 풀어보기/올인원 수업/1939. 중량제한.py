# 다리의 개수 M은 최대 100,000이며, 중량 제한 C는 최대 1,000,000,000입니다.
# 이진 탐색을 이용하여 O(M*logC)에 문제를 해결할 수 있습니다.
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 이진 탐색으로 찾습니다.

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y,weight))
    adj[y].append((x,weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while(start<=end):
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

