import sys

input = sys.stdin.readline

"""
 [로봇 청소기]
 board 정보 -> 0: 빈 칸, 1: 벽, 2: 청소한 공간
 step: 회전 카운트. 4가 되면 한 바퀴 돌아 다시 제자리로 돌아왔음을 의미
 항상 첫 행, 마지막 행, 첫 열, 마지막 열은 벽이라고 문제에서 주어졌으므로 범위 검사를 할 필요가 없음
"""


def cnt_clean_robot(r, c, d, board):            # 청소 함수
    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]                          # x, y 이동 거리 좌표
    dc = [0, 1, 0, -1]

    step = ans = 0                              # 초기 변수 지정

    while True:                                 # 조건이 True일 경우
        if board[r][c] == 0:                    # 아직 청소하지 않은 보드라면
            board[r][c] = 2                     # 청소 표시
            ans += 1                            # 청소한 칸 증가

        if step == 4:                           # 네 방향 확인했다면
            if board[r - dr[d]][c - dc[d]] == 1:    # 뒤가 벽이라면
                return ans                      # 청소한 칸 반환

            r -= dr[d]                          # 뒤로 한 칸 후진
            c -= dc[d]                          # 뒤로 한 칸 후진
            step = 0                            # 회전 카운트 초기화
        else:                                   # 그렇지 않다면
            d = (d + 3) % 4                     # 회전 방향 지정
            if board[r + dr[d]][c + dc[d]]:     # 회전 방향을 이미 청소했거나, 벽이라면
                step += 1                       # 회전
                continue

            r += dr[d]                          # 왼쪽 칸으로 이동
            c += dc[d]                          # 왼쪽 칸으로 이동
            step = 0                            # 회전 방향 초기화


# 입력
n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]     # 맵 세팅

# 연산 + 출력
print(cnt_clean_robot(r, c, d, board))                          # 값 연산 후 출력