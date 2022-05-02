import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_value = 0
arr_sum = [0]

for a in arr:
    # 값을 받을 때 합을 저장하는 배열 만들기
    sum_value += a
    arr_sum.append(sum_value)

for _ in range(m):
    a, b = map(int, input().split())
    print(arr_sum[b]-arr_sum[a-1])