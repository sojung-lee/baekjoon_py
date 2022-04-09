n, a = int(input()), {i: 1 for i in map(int, input().split())} #dic - 쪼개서 int로 한다음 있으면 1
#print(a)
m = input()
for i in list(map(int, input().split())):
    print(a.get(i,0))
