n = int(input())
stack = []
result = []
cnt = 1
temp = True
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append("+")
        cnt+=1

    if stack[-1] == num:
        stack.pop()
        result.append("-")

    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)


