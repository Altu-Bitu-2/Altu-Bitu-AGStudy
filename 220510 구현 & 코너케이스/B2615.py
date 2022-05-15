import sys
input = sys.stdin.readline

field = [list(map(int, input().split())) for _ in range(19)]


# 좌표의 유효성 검사
def valid_coord(x, y):
    return True if 0 <= x < 19 and 0 <= y < 19 else False


# 방향의 이전 돌이 같은 색일 경우 => 이미 검사 완료한 돌
def check_not_first(x, y, color, direction):
    if direction == 'row' and valid_coord(x, y-1) and field[x][y-1] == color:
        return False
    elif direction == 'col' and valid_coord(x-1, y) and field[x-1][y] == color:
        return False
    elif direction == 'right' and valid_coord(x-1, y-1) and field[x-1][y-1] == color:
        return False
    elif direction == 'left' and valid_coord(x-1, y+1) and field[x-1][y+1] == color:
        return False

    return True


# 연속된 5개의 돌 체크
def make5line(x, y, color, direction):
    count = 0
    # 시작 좌표
    pos = [x+1, y+1]

    if not check_not_first(x, y, color, direction):
        return False

    while valid_coord(x, y) and field[x][y] == color:
        count += 1
        # 행일 경우
        if direction == 'row':
            y += 1
        elif direction == 'col':
            x += 1
        elif direction == 'right':
            x += 1
            y += 1
        else:
            x += 1
            y -= 1
            # 왼쪽 아래 방향으로 검사할 경우 출력해야 하는 좌표 변경
            pos = [x, y+2]

    # 연달아 5개가 있을 경우 True
    if count == 5:
        print(color)
        print(*pos)
        return True

    return False


def solution():
    # 가로, 세로, 대각선 방향으로 완전 탐색하면서 연속된 수 찾기
    for i in range(19):
        for j in range(19):
            # 돌이 있다면
            if field[i][j] != 0:
                if make5line(i, j, field[i][j], 'row'):
                    return True
                if make5line(i, j, field[i][j], 'col'):
                    return True
                if make5line(i, j, field[i][j], 'right'):
                    return True
                if make5line(i, j, field[i][j], 'left'):
                    return True

    # 완성을 한 번도 못 시켰다면
    return False


if not solution():
    print(0)