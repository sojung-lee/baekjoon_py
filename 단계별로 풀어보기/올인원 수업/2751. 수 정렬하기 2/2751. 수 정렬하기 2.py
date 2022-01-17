#데이터의 개수가 최대 1,000,000개입니다
#시간 복잡도 O(NlogN)의 정렬 알고리즘을 이용해야 합니다
#고급 정렬 알고리즘 (병합 정렬, 퀵 정렬, 힙 정렬 등)을 이용하여 문제를 해결할 수 있습니다
#혹은 파이썬의 기본 정렬 라이브러리를 이용하여 문제를 풀 수 있습니다
#메모리가 허용된다면, 되도록 Python3보다는 PyPy3를 선택하여 코드를 제출합니다

#병합 정렬(Merge Sort)알고리즘
#- 분할 정복(Divide & Conquer)방식을 이용합니다
#- 절반씩 합치면서 정렬하면, 전체 리스트가 정렬됩니다
#- 시간 복잡도 O(NlogN)을 보장합니다

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i] <right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)

