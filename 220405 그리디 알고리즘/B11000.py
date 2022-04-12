import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
time = [list(map(int, input().split())) for _ in range(n)]

# 시작 시간 순으로 정렬
time.sort()

for t in time:
    heapq.heappush(heap, t[1])
    # 가장 빠르게 시작할 수 있는 시간이 시작 해야 하는 시간보다 크다면 강의실 추가
    if heap[0] <= t[0]:
        heapq.heappop(heap)

print(len(heap))