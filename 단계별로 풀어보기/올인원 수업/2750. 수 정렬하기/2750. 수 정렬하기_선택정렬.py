#1. 데이터의 개수가 1000개 이하이므로 기본적인 정렬 알고리즘으로 해결할 수 있습니다.
# 선택 정렬 알고리즘으로 문제 해결하기

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index]

    for i in array:
        print(i)
