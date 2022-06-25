import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []


def find_parent(x):
    if parent[x] < 0:
        return x
    return find_parent(parent[x])


def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return False

    if px > py:
        parent[px] += parent[py]
        parent[py] = px

    else:
        parent[py] += parent[px]
        parent[px] = py

    return True


for idx in range(1, m+1):
    x, y = map(int, input().split())
    graph.append([x, y, idx])

answer = []

for i in range(k):
    parent = [-1 for _ in range(n+1)]
    count = 0
    dist = 0

    # 가중치가 작은 간선부터 하나씩 제거
    for g in graph[i:]:
        x, y, weight = g

        if union_parent(x, y):
            count += 1
            dist += weight

    # n-1개의 정점을 연결할 수 있었을 때
    if count == n-1:
        answer.append(dist)
    else:
        answer.append(0)

print(*answer)