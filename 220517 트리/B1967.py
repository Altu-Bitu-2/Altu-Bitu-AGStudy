import sys
# 10**6 허용으로 하면 메모리 초과
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

n = int(input())
graph = [[] * n for i in range(n+1)]
leaf = [False] + [True for _ in range(n)]
distance = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().split())

    # 노드의 연결 정보 저장
    graph[a].append([b, d])
    graph[b].append([a, d])
    # 부모 노드라면 리프 노드 False
    leaf[a] = False

# 가장 첫번째 리프 노드 인덱스
start = leaf.index(True)
max_distance = 0


# DFS로 가장 거리가 먼 노드 계산
def long_distance(v, d):
    for g in graph[v]:
        node, dist = g
        if distance[node] == 0:
            distance[node] = d + dist
            long_distance(node, d + dist)


long_distance(start, 0)

# 아무 리프 노드에서 가장 거리가 먼 노드 => 그것과 가장 거리가 먼 노드가 트리의 지름
vertex = distance.index(max(distance))

distance = [0 for _ in range(n+1)]
distance[vertex] = -1
long_distance(vertex, 0)

print(max(distance))