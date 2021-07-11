import sys

def n_and_m(end: int, max_depth: int, current_stack: list):
    for i in range(1, end+1):
        if i in current_stack:
            continue

        current_stack.append(i)

        if len(current_stack) == max_depth:
            print(*current_stack)
        else:
            n_and_m(end, max_depth, current_stack)

        current_stack.pop()

end, max_depth = [int(value) for value in sys.stdin.readline().rstrip().split()]
stack = list()
n_and_m(end,max_depth,stack)