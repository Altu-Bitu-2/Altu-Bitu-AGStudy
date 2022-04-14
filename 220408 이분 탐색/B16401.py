import sys
input = sys.stdin.readline


def binary_search(m, snack):
    if sum(snack) < m:
        return 0

    start = 0
    end = snack[-1]
    result = 0

    while start <= end:
        result = 0
        mid = (start + end) // 2
        for s in snack:
            result += s // mid
        # 나눈 과자의 수가 아이들보다 많거나 같으면
        if result >= m:
            result = mid
            start = mid + 1
        elif result < m:
            end = mid - 1

    return result


# 조카의 수, 과자의 수
m, n = map(int, input().split())

# 과자의 길이
snack = list(map(int, input().split()))

snack.sort()

if m <= n:
    print(snack[len(snack)-m])
else:
    print(binary_search(m, snack))
