import sys
input = sys.stdin.readline


def solution(weight):
    weight.sort()
    max_value = weight[0]

    if max_value != 1:
        return 1

    for w in weight[1:]:
        nxt = w
        # 다음으로 시작할 숫자가 이전에 만든 최댓값 + 1보다 크다면 그 사이의 있는 값들을 만들 방법이 없음
        if nxt > max_value + 1:
            return max_value + 1
        max_value += nxt

    return max_value + 1


n = int(input())

print(solution(list(map(int, input().split()))))
