import sys
from collections import deque
input = sys.stdin.readline

field = [list(input().rstrip()) for _ in range(12)]
visited = [[False] * 6 for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 알파벳 아래에 '.'이 있으면 알파벳을 아래로 떨어뜨림
def chain():
    for l in range(6):
        for m in range(10, -1, -1):
            for n in range(11, m, -1):
                if field[m][l] != '.' and field[n][l] == '.':
                    field[n][l] = field[m][l]
                    field[m][l] = '.'
                    break


# BFS
def bfs(a, b, color):
    count = 1
    bomb = [[a, b]]
    queue = deque([(a, b)])
    visited[a][b] = True

    # BFS로 연결된 뿌요 탐색
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                bomb.append([nx, ny])
                count += 1

    # 4개 이상 모이면 뿌요를 터뜨림
    if count >= 4:
        for b in bomb:
            k, l = b[0], b[1]
            field[k][l] = '.'

    return count


checked = True
answer = 0

# 뿌요판이 변하지 않을 때까지 반복
while checked:
    checked = False
    # 모든 영역 순회
    for i in range(12):
        for j in range(6):
            # 뿌요를 탐색
            if field[i][j] != '.':
                count = bfs(i, j, field[i][j])
                # 뿌요가 한 번이라도 터졌다면 체크
                if count >= 4:
                    checked = True
    # 뿌요판 방문 초기화
    visited = [[False] * 6 for _ in range(12)]
    # 한 번 순회한 후 뿌요에 중력 적용
    chain()
    answer += 1

print(answer-1)