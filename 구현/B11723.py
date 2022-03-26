import sys
input = sys.stdin.readline

n = int(input())

check = [False] * 21

for _ in range(n):

    value = input().rstrip()

    if value == 'all':
        check = [True] * 21
        continue
    if value == 'empty':
        check = [False] * 21
        continue

    operator, num = value.split()
    num = int(num)

    if operator == 'add':
        check[num] = True
    elif operator == 'remove':
        check[num] = False
    elif operator == 'check':
        if check[num]:
            print(1)
        else:
            print(0)
    else:
        if check[num]:
            check[num] = False
        else:
            check[num] = True
