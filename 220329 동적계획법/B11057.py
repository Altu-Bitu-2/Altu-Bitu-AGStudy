import sys
input = sys.stdin.readline

n = int(input())

d = [[1] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 10):
        d[i][j] = d[i][j-1] + d[i-1][j]

print(d[n][9] % 10007)