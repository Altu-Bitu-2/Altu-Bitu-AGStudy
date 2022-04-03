import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [0] * 1001

answer = 0

for i in range(n):
    min_value = 0
    for j in range(i):
        # 앞에서 작은 수 중에 길이가 가장 긴 값을 선택
        if a[j] < a[i] and min_value < d[j]:
            min_value = d[j]
    d[i] = min_value + 1
    answer = max(d[i], answer)

print(answer)
