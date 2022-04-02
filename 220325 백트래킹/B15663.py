# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 수열 => 사전 순으로 증가
a.sort()

visited = [False] * n

arr = []
result = []


def backtracking():
    # 종료 조건

    if len(arr) == m:
        v = ' '.join(map(str, arr))
        if v not in result:
            result.append(v)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(a[i])
            backtracking()
            visited[i] = False
            arr.pop()


backtracking()

for r in result:
    print(r)
