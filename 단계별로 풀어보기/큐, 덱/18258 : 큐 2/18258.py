import sys
input = sys.stdin.readline

n = int(input())
queue = []
cnt = 0
for i in range(n):
    name = input().strip()
    if name.split()[0] == 'push':
        queue.append(int(name.split()[1]))

    elif name.split()[0] == 'pop':
        if len(queue) - cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif name.split()[0] == 'size':
        print(len(queue)-cnt)
    elif name.split()[0] == 'empty':
        if len(queue)-cnt == 0:
            print(1)
        else:
            print(0)
    elif name.split()[0] == 'front':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
    elif name.split()[0] == 'back':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[-1])

