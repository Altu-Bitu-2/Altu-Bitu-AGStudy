import sys
input = sys.stdin.readline

n = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))

# 처음 도시에서 출발
cost = edge[0] * node[0]
prev = node[0]

for i in range(1, n-1):
    # 이전 도시의 기름 값이 이번 도시보다 비싸면, 이번 도시에서 충전
    if prev > node[i]:
        prev = node[i]
    cost += prev * edge[i]

print(cost)
