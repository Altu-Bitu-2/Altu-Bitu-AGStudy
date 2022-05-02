import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
section_normal = [list(input()) for _ in range(n)]
section_blind = [[''] * n for _ in range(n)]
visited_normal = [[False] * n for _ in range(n)]
visited_blind = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전체 영역 확인
def find(section, visited):
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited = bfs(section, visited, i, j, section[i][j])
                count += 1
    return count


def bfs(section, visited, a, b, color):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and section[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return visited

# 적록색맹의 경우 R을 G로 변경
for i in range(n):
    for j in range(n):
        if section_normal[i][j] == 'R':
            section_blind[i][j] = 'G'
        else:
            section_blind[i][j] = section_normal[i][j]


normal = find(section_normal, visited_normal)
blind = find(section_blind, visited_blind)

print(normal, blind)