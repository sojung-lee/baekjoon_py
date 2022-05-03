S, tot = input(), 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        tot += 1
print((tot+1)//2)