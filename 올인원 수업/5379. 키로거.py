#1. 스택 두 개를 만들고, 스택 두 개의 중간 지점을 켜셔(cursor)fh rkswngkqslek.
#2. 문자 입력 : 왼쪽 스택에 원소를 삽입합니다.
#3. -입력 : 왼쪽 스택에 원소를 삽입합니다.
#4. <입력 : 왼쪽 스택에서 오른쪽 스택으로 원소를 이동합니다.
#5. >입력 : 오른쪽 스택에서 왼쪽 스택으로 원소를 이동합니다.
test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))