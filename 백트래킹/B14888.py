# N개의 수로 이루어진 수열
# N-1개로 이루어진 연산자
# 주어진 수의 순서 바꿀 수 없음
# 나눗셈은 몫만 취한다
# 음수를 양수로 나눌 때는 c++14 기준을 따른다 (파이썬도 동일? 아마.)
# 식의 결과 최대 최소 구하기

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
op = list(map(int, input().split()))

low = int(1e9)
high = -int(1e9)


def backtracking(depth, result, plus, minus, multiple, division):

    global low, high

    if depth == n:
        low = min(result, low)
        high = max(result, high)
        return

    if plus:
        backtracking(depth + 1, result + a[depth], plus - 1, minus, multiple, division)
    if minus:
        backtracking(depth + 1, result - a[depth], plus, minus - 1, multiple, division)
    if multiple:
        backtracking(depth + 1, result * a[depth], plus, minus, multiple - 1, division)
    if division:
        backtracking(depth + 1, int(result / a[depth]), plus, minus, multiple, division - 1)


backtracking(1, a[0], op[0], op[1], op[2], op[3])

print(high)
print(low)
