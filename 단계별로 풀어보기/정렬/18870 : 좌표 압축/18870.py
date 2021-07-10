import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}
print(dic)
for i in arr:
    print(dic[i], end =' ')


#for _ in enumerate(t):
#반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
