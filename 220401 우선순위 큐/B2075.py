import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
checked = [False] * n

table = list(map(int, input().split()))
heapq.heapify(table)

# 역순으로 리스트 탐색
for _ in range(n-1):
    line = map(int, input().split())
    # 상위 N개 중 가장 작은 수보다 커야 힙에 삽입할 수 있다.
    for x in line:
        if x > table[0]:
            heapq.heappushpop(table, x)

print(table[0])
