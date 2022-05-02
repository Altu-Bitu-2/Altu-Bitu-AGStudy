import sys
input = sys.stdin.readline

# 슬라이딩 윈도우

n, k = map(int, input().split())

i = [0] * 1000000
max_pos = 0

for _ in range(n):
    g, x = map(int, input().split())
    i[x] = g
    max_pos = max(max_pos, x)

# 윈도우의 크기 지정
size = 2 * k + 1
window = sum(i[:size])
result = window

# 윈도우가 하나씩 밀릴 때마다 추가하는 값 더해주고, 빠지는 값 빼줌.
for k in range(size, max_pos+1):
    window += i[k] - i[k-size]
    result = max(window, result)

print(result)
