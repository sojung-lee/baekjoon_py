#2. 파이썬의 기본 정렬 라이브러리로 문제 해결하기

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)