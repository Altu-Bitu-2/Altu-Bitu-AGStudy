import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n+1):
    weight = stuff[i][0]
    value = stuff[i][1]

    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])

