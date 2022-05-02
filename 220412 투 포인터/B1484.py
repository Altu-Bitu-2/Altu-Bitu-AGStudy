import sys
import math
input = sys.stdin.readline

g = int(input())

start = math.ceil(math.sqrt(g))
end = math.ceil(math.sqrt(100000))
answer = []

left, right = 1, 2

# sqrt(g)부터 탐색 시작
while left < right:
    diff = right**2 - left**2

    # 현재 차이가 g 킬로그램보다 크다면 왼쪽을 한 칸 키워 차이를 감소
    if diff > g:
        left += 1
    else:
        if diff == g:
            answer.append(right)
        right += 1

if answer:
    print(' '.join(map(str, answer)))
else:
    print(-1)
