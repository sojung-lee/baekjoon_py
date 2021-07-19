import sys
input = sys.stdin.readline

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(p[i])):
        if j == 0:
            p[i][j] += p[i-1][j]
        elif j == i:
            p[i][j] += p[i-1][j-1]
        else:
            p[i][j] += (max(p[i-1][j],p[i-1][j-1]))
print(max(p[n-1]))

