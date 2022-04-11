import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

count = 0

for _ in range(n):
    p, l = map(int, input().split()) # l => 최대 인원
    arr = list(map(int, input().split()))

    # 현재 신청 인원이 제한 인원보다 적다면 마일리지 1 사용
    if p < l:
        result.append(1)
        continue

    arr.sort(reverse=True)
    result.append(arr[l-1])

result.sort()
sum_value = 0

# 정렬 후 가장 작은 것부터 확인
for r in result:
    sum_value += r
    if sum_value > m:
        break
    count += 1

print(count)
