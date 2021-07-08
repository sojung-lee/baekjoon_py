n = int(input())
result = 0
for i in range(1,n+1):
    m = list(map(int, str(i)))
    sum_num = i + sum(m)
    if sum_num == n:
        result = i
        break
print(result)
