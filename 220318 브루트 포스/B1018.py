n, m = map(int, input().split())

chess = []

for _ in range(n):
    chess.append(input())

w = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']


def white_chess(x, y):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if chess[i][j] != w[i-x][j-y]:
                count += 1
    if count > 32:
        return 64 - count
    return count


answer = int(1e9)


for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, white_chess(i, j))

print(answer)