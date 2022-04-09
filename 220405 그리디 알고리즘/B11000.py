import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []
heap = []

for _ in range(n):
    time.append(list(map(int, input().split())))

# 시작 시간 순으로 정렬
time.sort()

heapq.heappush(heap, time[0][1])
count = 1

for t in time[1:]:
    heapq.heappush(heap, t[1])
    # 가장 빠르게 시작할 수 있는 시간이 시작해야 하는 시간보다 크다면 강의실 추가
    if heap[0] > t[0]:
        count += 1
    else:
        heapq.heappop(heap)

print(count)