import sys
input = sys.stdin.readline

INF = int(1e9)
# 임의로 주어진 두 정점은 반드시 통과해야 한다.

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
vertex = [['-'] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    vertex[a][b] = b
    vertex[b][a] = a

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist = graph[i][k] + graph[k][j]
            if graph[i][j] > dist:
                graph[i][j] = dist
                # 이전 집하장 값
                vertex[i][j] = vertex[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            vertex[i][j] = '-'
        print(vertex[i][j], end=' ')
    print()
