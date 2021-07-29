n = int(input()) #약수의 개수
a = list(map(int, input().split()))
max_num = max(a)
min_num = min(a)
print(max_num * min_num)
