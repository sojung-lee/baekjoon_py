n, b = int(input(), list(map(int, input().split())))

a = [b[0]]

for i in range(1, n):
    a.append(b[i] + (i + 1) - sum(a))

for i in a:
    print(i, end = ' ')