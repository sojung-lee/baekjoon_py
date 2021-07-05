import math
while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    elif (math.pow(a,2) + math.pow(b,2)) == math.pow(c,2):
        print('right')
    else: print('wrong')

    #빗변의 길이 가장 긴 것을 c로 설정해야함 이 과정 안해서 틀림

