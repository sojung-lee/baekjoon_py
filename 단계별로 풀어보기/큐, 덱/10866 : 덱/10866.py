import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dq = deque()

for _ in range(n):
    order = list(input().split())

    if order[0] == 'push_front':
        dq.appendleft(order[1])
    elif order[0] == 'push_back':
        dq.append(order[1])
    elif order[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif order[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif order[0] == 'size':
        print(len(dq))

    elif order[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif order[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])