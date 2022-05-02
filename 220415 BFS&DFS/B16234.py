## 예외 케이스를 찾지 못해 아직 통과하지 못했음

import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
number = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def federation(people):
    for k in range(n):
        for l in range(n):
            # 연합한 국가의 인구 맞춰주기
            if visited[k][l]:
                number[k][l] = people


def bfs(number, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    population = number[x][y]
    count = 1

    while queue:
        # 아직 방문하지 않았다면
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 네 방향 탐색
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 인구 차이가 l 이상 r 이하 라면
            if l <= abs(number[x][y] - number[nx][ny]) <= r:
                # 국경 열고 연결
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    # 연결된 칸 수, 칸의 인구 수
                    count += 1
                    population += number[nx][ny]

    # 이어진 모든 영역 탐색이 끝날 경우
    if count == 1:
        return 0
    # 연합한 국가가 있다면 인구 수 / 나라로 반환
    else:
        return int(population / count)


answer = 0

# 더 탐색할 곳이 없을 때까지
while True:
    checked = False
    for i in range(n):
        for j in range(n):
            # 연합 인원 수
            if not visited[i][j]:
                people = bfs(number, i, j)
                # 분배할 인원이 있다면 재분배
                if people != 0:
                    checked = True
                    federation(people)
    # 국경 닫기
    visited = [[False] * n for _ in range(n)]

    if checked:
        answer += 1
    else:
        break

print(answer)