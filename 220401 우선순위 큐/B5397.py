from collections import deque
t = int(input())

for _ in range(t):
    arr = list(map(str, input()))
    answer = deque()
    temp = deque()
    idx = 0

    for a in arr:
        if a == '<':
            if answer:
                temp.append(answer.pop())
        elif a == '>':
            if temp:
                answer.append(temp.pop())
        elif a == '-':
            if answer:
                answer.pop()
        else:
            answer.append(a)

    while temp:
        answer.append(temp.pop())

    print(''.join(answer))
