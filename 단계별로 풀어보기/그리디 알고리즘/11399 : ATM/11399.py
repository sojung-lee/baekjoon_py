n = int(input())
s = list(map(int, input().split()))
cnt = 0
result = 0
s.sort() #오름차순으로 정리
for i in range(n):
    cnt += s[i]
    result += cnt

print(result)