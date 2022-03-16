import sys
import math


def avg(num):
    return round(sum(num) / n)


def mid(num):
    # 정렬 후 중간값 계산
    num.sort()
    return num[math.floor(n/2)]


def mode(num):

    mod = dict()

    # dict로 빈도 체크
    for n in num:
        if n not in mod:
            mod[n] = 1
        else:
            mod[n] += 1

    # 빈도 순, 숫자 오름차순으로 정렬
    mod = sorted(mod.items(), key=lambda x: (-x[1], x[0]))

    # 길이가 1인 경우, 처음과 두번째의 최빈값이 다른 경우
    if len(mod) == 1 or mod[0][1] != mod[1][1]:
        return mod[0][0]
    else:
        return mod[1][0]


def ran(num):

    num.sort()
    return num[-1] - num[0]


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    num = []

    for _ in range(n):
        num.append(int(input()))

    print(avg(num))
    print(mid(num))
    print(mode(num))
    print(ran(num))