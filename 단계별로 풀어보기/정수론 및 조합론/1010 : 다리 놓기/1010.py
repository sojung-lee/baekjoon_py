from math import factorial
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    bridge = factorial(b) // (factorial(a)*factorial(b-a))
    print(bridge)