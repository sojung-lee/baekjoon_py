from itertools import combinations

n,m = map(int, input().split())
p = combinations(range(1, n+1),m)
for i in p:
    print(*i)