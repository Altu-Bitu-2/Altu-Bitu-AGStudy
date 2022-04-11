import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
waiting = [deque() for _ in range(m)]

for idx in range(n):
    d, h = map(int, input().split())
    # 사장이 나눈 줄번호
    line = idx % m
    waiting[line].append((-d, -h, line, idx))

count = 0
leading = []

# 가장 첫 번째 사람 비교하기 위헤 deque의 첫번째를 꺼냄
for w in waiting:
    if w:
        heapq.heappush(leading, w.popleft())

# idx == k (데카의 차례) 까지 진행
while leading[0][-1] != k:
    count += 1
    person = heapq.heappop(leading)
    line = person[2]
    # 화장실을 이용했다면, 다음으로 서 있던 사람을 heap에 삽입
    if waiting[line]:
        heapq.heappush(leading, waiting[line].popleft())

print(count)