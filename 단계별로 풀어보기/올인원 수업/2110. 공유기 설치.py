#집의 개수 N은 최대 200,000이며, 집의 좌표 X는 최대 1,000,000,000입니다.
#이진 탐색을 이용하여 O(N*logX)에 문제를 해결할 수 있습니다.
#가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾습니다.

n, c = list(map(int, input().split(' ')))

array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0]  #min 값
end = array[-1] - array[0]  #max 값
result = 0

while(start<=end):
    mid = (start + end)//2   #gap을 의미
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

            if count >= c: #c개 이상의 공유기를 설치할 수 있는 경우
                start = mid + 1
                result = mid

            else: #c개 이상의 공유기를 설치할 수 없는 경우
                end = mid - 1

print(result)

