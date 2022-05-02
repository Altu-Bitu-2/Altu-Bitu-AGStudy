import sys
input = sys.stdin.readline

# 접시 수, 초밥 가짓수, 연속 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())

rice = [int(input()) for _ in range(n)]
kind = [0] * (d+1)
count = 0

# 윈도우 영역 내에 있는 초밥 => 먹음
for i in range(k):
    kind[rice[i]] += 1
    if kind[rice[i]] == 1:
        count += 1

# 현재 초밥 종류 개수
answer = 0

for i in range(k, n+k-1):
    i %= n

    # 새로운 초밥이 없었을 경우에만
    if kind[rice[i]] == 0:
        count += 1

    # 새로운 초밥 추가, 빠질 초밥 제거
    kind[rice[i]] += 1
    kind[rice[i-k]] -= 1

    # 초밥 빼고 하나도 안 남았으면 카운트 감소
    if kind[rice[i-k]] == 0:
        count -= 1

    # 쿠폰 초밥 없어지면 추가해주기
    if kind[c] == 0:
        kind[c] = 1
        count += 1

    answer = max(answer, count)

print(answer)