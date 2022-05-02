import sys
from collections import deque
input = sys.stdin.readline

# INPUT
n = int(input())
area = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(area, a, b):
    cnt = 1
    queue = deque([(a, b)])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and area[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and area[i][j]:
            # 탐색하는 영역의 개수를 반환
            cnt = bfs(area, i, j)
            answer.append(cnt)

answer.sort()

# OUTPUT
print(len(answer))

for a in answer:
    print(a)