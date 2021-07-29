def five_count(n):
    ans = 0
    while n != 0:
        n = n//5
        ans += n
    return ans

def two_count(n):
    ans = 0
    while n != 0:
        n = n//2
        ans += n
    return ans

n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))