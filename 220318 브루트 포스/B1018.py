n, m = map(int, input().split())

chess = []

for _ in range(n):
    chess.append(input())

w = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
b = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']


def white_chess(x, y):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if chess[i][j] != w[i-x][j-y]:
                count += 1
    return count


def black_chess(x, y):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if chess[i][j] != b[i-x][j-y]:
                count += 1
    return count


answer = int(1e9)


for i in range(n-7):
    for j in range(m-7):
        # i와 j가 시작점, 흰색으로 시작했을 때와 검은색으로 시작했을 때 바꾸어야 할 영역의 계산해 최솟값
        value = min(white_chess(i, j), black_chess(i, j))

        if value < answer:
            answer = value

print(answer)