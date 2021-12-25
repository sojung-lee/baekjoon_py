#1. 데이터의 개수가 최대 10,000,000개입니다.
#2. 시간 복작도 O(N)의 정렬 알고리즘을 이용해야 합니다.
#3. 수의 범위가 1 ~ 10,000이므로 계수 정렬을 이용할 수 있습니다.

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)