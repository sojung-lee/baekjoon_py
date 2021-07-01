##시간초과
import math
while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if i == 1:
            continue
        elif i == 2:
            count += 1
            continue

        else:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                count += 1
                #for  안에 있는 break를 만나지 않고 for문 다 돌아서 나오게 되면 else문을 실행하게 되고
                #만약 break되서 중간에 나오면 else문이 실행되지 않음

    print(count)
