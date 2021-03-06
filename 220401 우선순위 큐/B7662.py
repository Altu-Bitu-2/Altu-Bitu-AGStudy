
# 데이터를 삭제할 때 연산 명령에 따라 우선 순위가 가장 높은 / 낮은 데이터 중 하나를 삭제한다.

import sys
import heapq
input = sys.stdin.readline

t = int(input())


def remove_invalid_data(heap):
    while heap and not is_valid[heap[0][1]]:
        heapq.heappop(heap)
    return


for _ in range(t):
    n = int(input())

    max_heap = []
    min_heap = []
    is_valid = []

    # 유효성 검사를 위한 인덱스
    idx = 0

    for _ in range(n):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            # 각각 힙 생성
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            # 유효성 검사 부분
            is_valid.append(True)
            idx += 1

        if op == 'D':
            # 힙이 비어 있으면 패스
            if not min_heap or not max_heap:
                continue

            # 최솟값을 삭제
            if num == -1:
                # 삭제 전에 max 큐에서 삭제된 숫자를 min 큐에도 반영
                remove_invalid_data(min_heap)
                # 가장 작은 값 삭제
                # 유효값 체크 배열을 False로
                if min_heap:
                    is_valid[heapq.heappop(min_heap)[1]] = False

            # 최대값을 삭제
            elif num == 1:
                remove_invalid_data(max_heap)
                if max_heap:
                    is_valid[heapq.heappop(max_heap)[1]] = False

    remove_invalid_data(max_heap)
    remove_invalid_data(min_heap)

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")