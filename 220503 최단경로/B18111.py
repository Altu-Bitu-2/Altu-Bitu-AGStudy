import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

time = 0
answer = [int(1e9), -int(1e9)]

low = min(map(min, field))
height = max(map(max, field))

# 현재 필드의 최대 높이 이상 쌓을 필요가 없음
for cur in range(low, height+1):
    time = 0
    block = b

    for row in field:
        for col in row:
            # 더 튀어 나와 있으면 제거, 아니라면 쌓아주기
            diff = col - cur
            if col > cur:
                time += diff * 2
                block += diff
            elif col < cur:
                time -= diff
                block += diff

    # 사용할 수 있는 블록의 개수보다 초과했을 때
    if block < 0:
        continue

    # 짧은 작업 시간, 높은 높이 순으로 확인
    if answer[0] > time:
        answer = [time, cur]
    elif answer[0] == time:
        answer[1] = max(answer[1], cur)

print(*answer)
