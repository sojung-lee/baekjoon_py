import sys
s1 = sys.stdin.readline().strip()  #strip을 안해주면 공백도 들어가버림..?
s2 = sys.stdin.readline().strip()

matrix = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])



#len1 = len(s1)
#len2 = len(s2)
#로 설정해서 하면 출력초과문제 해결 가능하다.