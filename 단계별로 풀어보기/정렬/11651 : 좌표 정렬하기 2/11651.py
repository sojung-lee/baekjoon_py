import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [a,b] = map(int, input().split())
    array.append([b,a])

sorted_array = sorted(array)

for i in range(n):
    print(sorted_array[i][1],sorted_array[i][0])