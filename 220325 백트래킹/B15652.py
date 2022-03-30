import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []


def backtracking(start):

    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n+1):
        arr.append(i)
        backtracking(i)
        arr.pop()


backtracking(1)