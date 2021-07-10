n = int(input())
# 길이가 짧은 것부터
# 길이가 같으면 사전 순
words_list = []
for i in range(n):
    word = str(input())
    word_cnt = len(word)
    words_list.append((word, word_cnt))

words_list = list(set(words_list))
#print(words_list)
words_list.sort(key = lambda word:(word[1],word[0]))
for word in words_list:
    print(word[0])



