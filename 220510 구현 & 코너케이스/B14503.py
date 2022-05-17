import sys
from collections import deque
input = sys.stdin.readline

# n, m 칸의 크기
n, m = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표, 방향 0:북, 1:동, 2:남, 3:서
r, c, d = map(int, input().split())

# 가는 모두 벽
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# # 북, 동, 남, 서
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# 북, 서, 남, 동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 벽 있는 곳은 방문한 곳으로 표시
for i in range(n):
    for j in range(m):
        if field[i][j]:
            visited[i][j] = True


def bfs(a, b, direction):
    queue = deque([(a, b)])
    visited[a][b] = True

    # d == 0이면 왼쪽, d == 1 이면 위, d == 2 이면 오른쪽, d == 3이면 아래 확인해야 함.
    while queue:
        x, y = queue.popleft()
        print(x, y, direction)
        # 다음 확인해야 할 곳
        for k in range(5):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 이미 네 번 돌았을 경우 후진
            if k == 4 and not field[nx][ny]:
                queue.append((x + dx[direction+1], y + dy[direction+1]))
                break
            # 갈 수 없다면
            if visited[nx][ny]:
                # 방향 회전
                direction = (direction + 1) % 4
            # 막혀 있지 않다면 큐에 추가하고 종료
            else:
                direction = (direction + 1) % 4
                visited[nx][ny] = True
                queue.append((nx, ny))
                break


    # 전부 돌았을 경우
    v_count = 0
    f_count = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                v_count += 1
            if field[i][j]:
                f_count += 1

    # 청소된 영역 확인
    return v_count - f_count


print(bfs(r, c, d))
