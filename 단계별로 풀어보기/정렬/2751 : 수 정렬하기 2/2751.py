#입력되는 수는 중복되지 않는다. -> python 내장함수 set사용

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

n_list = sorted(set(n_list))
for i in range(len(n_list)):
    print(n_list[i])

