def gcd(a,b):
    return gcd(b, a%b) if b else a

n = int(input())
s = list(map(int, input().split()))
for i in range(1, n):
    result = gcd(s[0],s[i])
    print('{}/{}'.format(s[0]//result, s[i]//result))