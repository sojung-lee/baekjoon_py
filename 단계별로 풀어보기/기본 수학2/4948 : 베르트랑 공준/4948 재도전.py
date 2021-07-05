def prime_num():
    nums = [i for i in range(2,123456*2+1)]
    prime_arr = []
    for num in nums:
        flag = True
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                flag = False
                break
        if flag:
            prime_arr.append(num)
    return prime_arr

arr = prime_num()
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for a in arr:
        if a>2*n:
            break
        elif n<a<=2*n:
            cnt += 1
    print(cnt)