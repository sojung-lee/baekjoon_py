n = int(input())
n_list = []
n_list = list(map(int, str(n)))
n_list.sort(reverse=True)
for i in n_list:
    print(i, end="")