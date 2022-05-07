# 🌏 최단 경로 (Shortest Path)
가장 짧은 경로를 찾는 알고리즘

### 다익스트라 최단 경로 알고리즘

- 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발해 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
- **'음의 간선'** 이 없을 때 정상적으로 동작.
- 시간 복잡도: O(V^2)
**O(V)** 번에 걸쳐 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다. 만약, 최단 거리의 정보를 힙에 담아 처리할 경우 **O(ElogV)**의 시간 복잡도로 일을 처리할 수 있다.

<br>

- 과정
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블을 갱신한다.



```
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접 노드 확인
        for i in graph[now]:
            # 가장 최단 거리가 짧은 노드 정보 꺼내 인접한 노드의 cost 값 업데이트
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

<br>

### 플로이드 워셜 알고리즘

- 모든 지점에서 다른 지점까지의 최단 경로를 모두 구해야하는 경우 사용한다.
- 시간 복잡도: O(N^3)
- D_(ab) = min(D_(ab), D_(ak) + D_(kb))
즉, a에서 b로 가는 비용과 a에서 k를 거쳐 b로 가는 비용 중 더 작은 것을 반복 선택한다.

```
INF = int(1e9)

# 노드의 개수 및 간선의 개수
n = int(input())
m = int(input())

# 2차원 그래프 생성 후 값 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 무한
        if graph[a][b] == INF:
            print("INFINITY", end='')
        else:
            print(graph[a][b], end='')
    
    print()
```

<br>

### 벨만-포드 알고리즘

- 하나의 시작점에서 모든 정점까지의 최단 경로를 구한다.
- 가중치에 **음의 간선** 이 있을 경우 다익스트라 대신 사용한다. 즉, 음수 사이클 존재 여부를 알 수 있다.
- 시간 복잡도: O(VE). 모든 정점을 V-1번 갱신한 뒤, 한 번 더 갱신을 시도한다.

<br>

- 과정
1. 시작 정점을 결정한다.
2. 시작 정점에서 각각 다른 정점까지의 거리 값을 무한대로 초기화한다.
3. 현재 정점에서 모든 인접 정점들을 탐색하며, 기존에 저장되어 있는 인접 정점까지의 거리보다 현재 정점을 거쳐 인접 정점에 도달하는 거리가 더 짧은 경우 갱신한다.
4. 위의 과정을 V-1번 반복하고, 이후 거리가 갱신되는 경우가 생기면 그래프에 음수 사이클이 존재하는 것이다.



```
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보
graph = []
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellman-ford(start):
    # 시작 노드의 거리를 0으로 초기화
    distance[start] = 0
    
    for i in range(n):
        for g in graph:
            node, next_node, cost = g[0], g[1], g[2]
            if dist[node] != INF and dist[nex_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n-1:
                    # n-1번 이후에도 반복이 계속된다면, 음의 사이클이 존재하는 것.
                    return True
    return False
    
dijkstra(start)

# 음의 간선이 있을 경우 -1 반환
if dijkstra(start):
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
```
