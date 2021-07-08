n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

for i in range(len(m)):
    for j in range(len(m)):
        if m[i]<m[j]:
            m[i], m[j] = m[j], m[i]

for i in m:
    print(i)