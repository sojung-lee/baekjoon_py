import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [a,b] = map(int,input().split())
    array.append([a,b])

sorted_array = sorted(array)

for i in range(n):
    print(sorted_array[i][0],sorted_array[i][1])