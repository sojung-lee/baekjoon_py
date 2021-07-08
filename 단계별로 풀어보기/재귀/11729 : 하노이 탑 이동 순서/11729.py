#하노이 탑 : 항상 작은 원반이 위에 있어야함


def hanoi(n,start,sub,end):
    if n == 1:
        print(start,end)
    else:
        hanoi(n-1,start,end,sub)
        print(start,end)
        hanoi(n-1,sub,start,end)


n = int(input())
sum = 1
for i in range(n-1):
    sum = sum*2+1
print(sum)
hanoi(n,1,2,3)