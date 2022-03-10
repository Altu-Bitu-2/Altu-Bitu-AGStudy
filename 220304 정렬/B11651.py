import sys

n = int(sys.stdin.readline())

cord = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    cord.append([x, y])

# y 좌표 먼저 정렬
cord.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(cord[i][0], cord[i][1])