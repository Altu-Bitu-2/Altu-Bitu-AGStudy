# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 백트래킹으로 풀 것!

n, m = map(int, input().split())

arr = []

def backtracking():
    # 시작 순서 받음
    # 현재 길이가 m이 되면 return (종료 조건)
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        backtracking()
        arr.pop()


backtracking()