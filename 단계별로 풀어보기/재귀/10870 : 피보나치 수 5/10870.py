#함수 사용

def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)
n = int(input())
print(fibo(n))
