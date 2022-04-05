import sys
input = sys.stdin.readline

n = int(input())

d = [0] * n+1

# n = 1일 때 칸을 채우는 경우의 수
d[1] = 1

# n = 2일 때 칸을 채우는 경우의 수
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 10007

print(d[n])