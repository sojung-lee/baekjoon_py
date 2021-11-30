from collections import deque
n, m = map(int, input().split())

data = deque([i for i in range(1, n+1)])
index = list(map(int, input().split()))

cnt = 0
for num in index:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data)//2:
                data.rotate(-1)
                cnt += 1
# rotate() 메소드는
# 양수 인수를 받으면 오른쪽 끝에 있는 항목을 지정한 개수만큼 왼쪽 끝으로 이동하고
# 음수 인수를 받으면 왼쪽 끝에 있는 항목을 지정한 개수만큼 오른쪽 끝으로 이동시킨다.
            else:
                data.rotate(1)
                cnt += 1
print(cnt)


