import sys
import heapq

input = sys.stdin.readline

n = int(input())
gift = []

for _ in range(n):
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        if not gift:
            print(-1)
        else:
            print(-heapq.heappop(gift))

    else:
        for a in arr[1:]:
            heapq.heappush(gift, -a)
