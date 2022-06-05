import sys
input = sys.stdin.readline

x, n = map(int, input().split())


def solution(x, n):
    if n != 1 and n % 2 != 0:
        return "ERROR"

    elif (n == 0 and x > 0) or (n == 1 and x < 0):
        return "INFINITE"

    elif x > 0 and n != 0 and n % 2 == 0:
        return (x-1) // (n//2)

    else:
        return "0"


print(solution(x, n))
