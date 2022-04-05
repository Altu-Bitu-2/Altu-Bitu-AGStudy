import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    d = [0 for _ in range(m+1)]

    d[0] = 1

    for a in arr:
        # 코인 리스트의 값보다 큰 경우 경우의 수를 추가
        for i in range(a, m+1):
            d[i] += d[i-a]

    print(d[m])
