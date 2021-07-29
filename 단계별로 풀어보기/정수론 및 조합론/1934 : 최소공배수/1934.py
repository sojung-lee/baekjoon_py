import sys
input = sys.stdin.readline

def gcd(a,b):
    return gcd(b,a%b) if b else a #b가 0이 아니면 gcd호출 0이면 a호출

def lcm(a,b):
    return a*b//gcd(a,b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a,b))

