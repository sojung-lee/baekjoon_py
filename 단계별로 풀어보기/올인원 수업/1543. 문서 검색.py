#문서의 길이는 최대 2,500이고 단어의 길이는 최대 50입니다.
#단순히 모든 경우의 수를 계산하여 문제를 해결할 수 있습니다.
#시간 복잡도 O(NM)의 알고리즘으로 해결할 수 있습니다.

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        index += len(word)

    else:
        index += 1

print(result)