import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x: x[2])
parent = [-1 for _ in range(n+1)]


def find_parent(x):
    # 값이 음수면 루트 정점
    if parent[x] < 0:
        return x
    return find_parent(parent[x])


def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    # 두 점이 이미 같은 집합에 속한다면 패스
    if px == py:
        return False

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px

    else:
        parent[py] += parent[px]
        parent[px] = py

    return True


min_dist = 0
max_weight = 0

for g in graph:
    if union_parent(g[0], g[1]):
        min_dist += g[2]
        max_weight = max(max_weight, g[2])

# 크루스칼 알고리즘으로 전부 연결한 후 가장 가중치가 큰 간선 하나 삭제해서 마을 분리
print(min_dist - max_weight)
