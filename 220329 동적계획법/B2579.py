import sys
input = sys.stdin.readline

n = int(input())
array = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = array[1]

# n이 1일 때 (array[2])가 없기 때문에 IndexError
dp[2] = array[1] + array[2]

if n == 1:
    print(array[1])

else:
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + array[i-1], dp[i-2]) + array[i]

        print(dp[n])