import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    # 1원 5원 10원 50원 100원 500원

    d = [0 for _ in range(m+1)]

    d[0] = 1

    for i in range(1, n+1):
        for j in range(a[i], m):
            d[j] += d[j-a[i]]

    print(d[m])
