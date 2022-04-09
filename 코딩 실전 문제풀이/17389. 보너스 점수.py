n, s = input(), input()

score, bonus = 0, 0
for idx, ox in enumerate(s): # 입력이 주어졌을 때 인덱스를 같이 반환
   # print(idx, ox)
    if ox == 'O':
        score += idx + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)