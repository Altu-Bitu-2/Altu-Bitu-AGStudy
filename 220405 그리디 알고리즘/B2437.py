import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))

weight.sort()


def solution(max_value):
    if max_value != 1:
        return 1

    for w in weight[1:]:
        nxt = w
        if nxt > max_value + 1:
            return max_value + 1
        max_value += nxt

    return max_value + 1


print(solution(weight[0]))
