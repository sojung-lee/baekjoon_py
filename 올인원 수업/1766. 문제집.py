# 본 문제는 전형적인 위상 정렬 문제이다
# 위상 정렬은 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정해주는 알고리즘이다.
# 위상 정렬의 시간 복잡도는 O(V+E)로 문제를 해결할 수 있다.

# 위상 정렬(topology sort) 알고리즘
# 1. 진입 차수가 0인 정점을 큐에 삽입합니다.
# 2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거합니다.
# 3. 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입합니다.
# 4. 큐가 빌 때까지 2,3과정을 반복

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것
# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

import heapq

n, m = map(int, input().split())
array = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y) # 어떤 노드가 연결되어있는지.
    indegree[y] += 1 # 연결 당한 노드

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop()
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end = ' ')