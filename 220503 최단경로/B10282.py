import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
# 테스트 케이스 개수
t = int(input())


def dijkstra(c):
    ans = 0
    queue = []
    # 시작 노드로 가는 최단 경로는 0
    heapq.heappush(queue, (0, c))

    distance[c] = 0

    while queue:
        # 가장 최단거리가 짧은 값 꺼내기
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # 다른 곳까지의 비용은 현재 거리 + 이어진 그래프의 거리
            cost = dist + i[1]
            # 이번에 계산한 비용이 기존 비용보다 작다면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
        ans = dist

    # 시간
    return ans


for _ in range(t):
    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터의 번호
    n, d, c = map(int, input().split())

    # 정보를 담을 리스트
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    time = dijkstra(c)

    # 감염된 컴퓨터 수
    count = 0
    for d in distance:
        if d != INF:
            count += 1

    print(count, time)
