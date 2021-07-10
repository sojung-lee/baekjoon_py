import sys
num = int(sys.stdin.readline())
n = []
for i in range(num):
    n.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(n)/len(n)))

#중앙값
n = sorted(n)
median = int(len(n)/2)
print(n[median])

#최빈값
from collections import Counter
cnt = Counter(n).most_common()
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])


#범위
print(n[-1]-n[0])