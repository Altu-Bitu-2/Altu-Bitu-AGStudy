import sys
input = sys.stdin.readline

INF = int(1e9)
# 임의로 주어진 두 정점은 반드시 통과해야 한다.

n, e = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 자신의 거리 0으로 초기화
for i in range(n+1):
    graph[i][i] = 0

# 통과해야 하는 두 개의 정점
s1, s2 = map(int, input().split())

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist = graph[i][k] + graph[k][j]
            if graph[i][j] > dist:
                graph[i][j] = dist

answer = min(graph[1][s1] + graph[s1][s2] + graph[s2][n], graph[1][s2] + graph[s2][s1] + graph[s1][n])

if answer >= INF:
    print(-1)
else:
    print(answer)
