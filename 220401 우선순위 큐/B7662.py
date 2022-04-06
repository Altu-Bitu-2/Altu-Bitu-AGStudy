# 데이터를 삭제할 때 연산 명령에 따라 우선 순위가 가장 높은 / 낮은 데이터 중 하나를 삭제한다.

import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    priority_queue = []
    remove = []
    max_heap = []
    min_heap = []

    for _ in range(n):
        op, num = input().split()
        num = int(num)
        priority_queue.append((op, num))

    for op, num in priority_queue:
        if op == 'I':
            # 각각 힙 생성
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))

        if op == 'D':
            # 삭제 여부... 반영?
            if not min_heap or not max_heap:
                continue
            if num == -1:
                remove.append(heapq.heappop(min_heap))
            elif num == 1:
                remove.append(heapq.heappop(max_heap)[1])

        print(remove, max_heap, min_heap, op, num)

    max_value = -int(1e9)
    min_value = int(1e9)

    for k, p in priority_queue:
        if p not in remove:
            min_value = min(p, min_value)
            max_value = max(p, max_value)

    if len(remove) == len(priority_queue):
        print("EMPTY")
    else:
        print(max_value, min_value)
