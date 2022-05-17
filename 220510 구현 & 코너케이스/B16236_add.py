import sys
from collections import deque

input = sys.stdin.readline

INF = 401

"""
 [아기 상어]
 1. 상어로부터 가장 가까운 거리에 있는 모든 물고기 탐색 (BFS)
 2. 우선순위 조건에 맞추어 먹으러 갈 물고기 확정
    탐색하는 방향에 우선순위를 두는 걸로 해결되지 않음! (예제 입력 4) 정렬 필요
 3. 상어가 이동할 수 있는 곳이 없을 때까지 BFS 탐색 반복
 입력 범위가 작기 때문에 매번 BFS 탐색을 반복해도 시간 초과 X
 가능한 물고기의 최대 마리 수 : 399마리
 최대 BFS 탐색 횟수 : 399회, 1회 탐색마다 while 문은 최대 400회 미만으로 순회
 총 연산 횟수 약 160000번으로 충분히 가능
 해설 : https://myunji.tistory.com/378
 *글 자체는 별로 도움이 안되고...그냥 리팩토링하면 코드가 이렇게 되는구나 정도만 봐주세요
"""


def next_pos(n, shark_size, shark, board):
    dr = [-1, 1, 0, 0]                          # dx 이동 좌표
    dc = [0, 0, -1, 1]                          # dy 이동 좌표

    min_dist = INF                              # 최단거리 최대로 초기화
    que = deque()                               # 상어가 갈 수 있는 곳
    dist = [[0] * n for _ in range(n)]          # 상어로부터의 거리 - 초기값은 0으로
    pos_list = []                               # 상어가 먹을 수 있는 물고기들의 위치

    dist[shark[0]][shark[1]] = 1                # 초기 거리 1
    que.append(shark)                           # 현재 상어 좌표를 queue에 추가

    while que:                                  # queue에 값이 존재하면
        row, col = que.popleft()                # row와 col 값 받아오기

        # 최단거리 이상은 탐색할 필요 없음
        if dist[row][col] >= min_dist:          # 최단거리 이상은 탐색하지 않음
            continue

        for i in range(4):                      # 네 방향 탐색
            nr = row + dr[i]                    # x 좌표 이동
            nc = col + dc[i]                    # y 좌표 이동
            # nr과 nc가 필드 값을 넘어갔거나 이미 거리를 확인했거나, 먹이의 크기가 상어 사이즈보다 큰 경우 패스
            if not (0 <= nr < n and 0 <= nc < n) or dist[nr][nc] or board[nr][nc] > shark_size:
                continue

            dist[nr][nc] = dist[row][col] + 1   # 거리를 1 증가

            # 먹을 수 있는 물고기 발견
            if board[nr][nc] and board[nr][nc] < shark_size:
                pos_list.append((nr, nc))       # 상어가 먹을 수 있는 물고기에 추가
                min_dist = dist[nr][nc]         # 최단 거리 갱신
                continue

            que.append((nr, nc))                # 다음 탐색 큐에 추가

    # 상어가 갈 수 있는 곳이 없다면
    if not pos_list:
        return min_dist, (-1, -1)               # 최단거리를 반환

    pos_list.sort()                             # 다음 갈 곳을 정렬

    return min_dist - 1, pos_list[0]            # 현재 좌표를 1부터 시작했으니 최단거리를 1 감소하고 다음 먹을 수 있는 물고기 반환


def simulation(n, shark, board):                # 인자로 n, shark, board 받아오기
    ans = cnt = 0                               # 먹은 물고기 수 0
    size = 2                                    # 상어의 초기 크기

    while True:                                 # True 일 동안 반복
        dist, pos = next_pos(n, size, shark, board)     # 다음으로 먹을 수 있는 물고기의 좌표와 거리 반환
        if dist == INF:                         # 더 이상 먹을 수 있는 물고기가 공간에 없으면
            break                               # 나감

        ans += dist                             # 반환된 거리를 결과에 추가
        cnt += 1                                # 먹은 물고기 증가

        if cnt == size:                         # 상어 크기 증가
            cnt = 0                             # 먹은 물고기 수 0
            size += 1                           # 상어 크기 증가

        # 상어 이동
        board[shark[0]][shark[1]] = 0           # 상어 이동
        shark = pos                             # 상어 좌표 변경

    return ans                                  # 결과 반환


# 입력
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)] # 맵 정보

for i in range(n):                              # n * n만큼 반복
    for j in range(n):
        if board[i][j] == 9:                    # 칸의 값이 9일 경우 상어의 위치
            shark_pos = (i, j)                  # 상어의 위치 (i, j)
            break                               # 종료

print(simulation(n, shark_pos, board))          # 결과 출력