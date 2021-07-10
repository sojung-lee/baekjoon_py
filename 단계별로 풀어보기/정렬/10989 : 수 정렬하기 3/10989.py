#dictionary 타입은 immutable한 키와 mutable한 값으로 맵핑되어 있는 순서가 없는 집합
#dict 예제
#new_dict = dict(alice=5,bob=20,tony=15,suzy=30)
#new_dict결과 {'alice':5, 'bob':20, 'tony':15, 'suzy':30}


n = int(input())
dict = {}

for i in range(n):
    num = int(input())
    if num not in dict.keys():
        dict[num] = 1
    else:
        dict[num] = dict[num]+1

sorted_dict = sorted(dict.items())

for i in range(len(sorted_dict)):
    for j in range(sorted_dict[i][1]):
        print(sorted_dict[i][0])