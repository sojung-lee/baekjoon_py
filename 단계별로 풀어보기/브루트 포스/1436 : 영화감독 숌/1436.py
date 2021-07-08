#666부터 1씩 증가시켜서 해당값이 나오면 출력하는 문제!
#6660이 6666보다 작음 그래서 7,13 순서임

n = int(input())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1

