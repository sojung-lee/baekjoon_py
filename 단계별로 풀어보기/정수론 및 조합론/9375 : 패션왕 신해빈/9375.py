n = int(input())
for _ in range(n):
    num = int(input())

    if num == 0:
        print(0)
        continue

    wearable = dict()
    for _ in range(num):
        wear_name, wear_type = map(str, input().split())

        if wear_type in wearable.keys():
            wearable[wear_type] += 1
        else:
            wearable[wear_type] = 1

        ans = 1
        for key in wearable.keys():
            ans *= (wearable[key]+1)

    print(ans-1)