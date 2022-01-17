# 1. 피보나치 수열의 점화식을 세웁니다.
# F0 = 0, F1 = 1
# Fn = Fn-1 + Fn-2 (n>=2)
# 2. 재귀 함수를 이용해 문제를 풀 수 있는지 검토해야 합니다.
# 3. 문제에서 N은 최대 45
# 재귀적 함수의 문제점 => 계속 그 전의 단계를 계산해야한다.
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(int(input()))) """


n = int(input())

a, b = 0, 1

while n>0:
    a,b = b, a+b
    n -= 1

print(a)