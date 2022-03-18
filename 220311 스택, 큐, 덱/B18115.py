import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
queue = deque([])

for i in range(1, n+1):
    # 역순으로 똑같이 진행
    # 1. 제일 위의 카드 하나를 바닥에 내려 놓는다 => 바닥의 카드를 위에 올린다.
    if arr[n-i] == 1:
        queue.appendleft(i)
    # 2. 위에서 두번째 카드를 바닥에 내려 놓는다 => 바닥의 카드를 위에서 두번째에 올린다.
    elif arr[n-i] == 2:
        queue.insert(1, i)
    # 3. 제일 밑에 있는 카드를 바닥에 내려 놓는다. => 바닥의 카드를 아래 내려 놓는다.
    else:
        queue.append(i)

for q in queue:
    print(q, end=' ')