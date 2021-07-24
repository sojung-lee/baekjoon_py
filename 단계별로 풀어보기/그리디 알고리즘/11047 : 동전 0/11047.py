a, b = map(int, input().split())
coin = []
cnt = 0
for i in range(a):
    coin.append(int(input()))

for i in range(a-1,-1, -1):
    if b == 0:
        break
    if coin[i] > b:
        continue
    cnt += b//coin[i]
    b %= coin[i]

print(cnt)