# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []


def backtracking():

    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        arr.append(i)
        backtracking()
        arr.pop()


backtracking()