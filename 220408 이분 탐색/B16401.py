import sys
input = sys.stdin.readline


def binary_search(m, snack):
    # 조카의 수, 과자

    left = 1
    # 가장 긴 과자의 길이
    right = snack[-1]

    while left <= right:
        mid = (left + right) // 2
        result = 0
        # 만들 수 있는 과자의 수
        for s in snack:
            result += s // mid
        # 만약 나눠줄 수 있는 과자의 수가 조카의 수보다 많다면
        if result >= m:
            # 과자 길이 증가
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


# 조카의 수, 과자의 수
m, n = map(int, input().split())

# 과자의 길이
snack = list(map(int, input().split()))
snack.sort()

print(binary_search(m, snack))