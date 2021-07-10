n = int(input())
n_list = []
#나이순
#가입한 순
for i in range(n):
    x, y = map(str,input().split())
    x = int(x)
    n_list.append((x,y))

n_list.sort(key = lambda member:(member[0]))
for member in n_list:
    print(member[0],member[1])