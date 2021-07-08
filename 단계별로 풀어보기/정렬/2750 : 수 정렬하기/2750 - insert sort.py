n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

for i in range(1,len(m)):
    while(i>0) & (m[i]<m[i-1]):
        m[i],m[i-1] = m[i-1],m[i]
        i -= 1

for n in m:
    print(n)
