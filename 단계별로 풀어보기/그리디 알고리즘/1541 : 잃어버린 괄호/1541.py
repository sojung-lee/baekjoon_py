n = input().split('-')
sum = 0
if n[0] == '':
    n[0] = '0'
for i in n[0].split('+'):
    sum += int(i)

for i in n[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
