import sys
import math
input = sys.stdin.readline

g = int(input())

start = math.ceil(math.sqrt(g))
end = math.ceil(math.sqrt(100000))
answer = []

# sqrt(g)부터 탐색 시작
for k in range(start, g):
    value = math.sqrt(pow(k, 2) - g)
    # 제곱근이 정수라면 정답
    if value == int(value) and value != 0:
        answer.append(k)

if answer:
    print(' '.join(map(str, answer)))
else:
    print(-1)
