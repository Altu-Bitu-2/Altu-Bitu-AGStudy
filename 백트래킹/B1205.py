import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())

if n > 0:
    score = list(map(int, input().split()))

    rank = 0
    tie = 0

    for i in range(n):
        if score[i] > new:
            rank += 1
        # 동점자
        elif score[i] == new:
            tie += 1
        else:
            break

    # 점수 높은 사람 + 동점자의 수가 p를 넘으면 랭킹에 등재되지 못함
    if rank + tie >= p:
        answer = -1
    else:
        answer = rank + 1

    print(answer)

# p > 0 이므로 한 명도 랭킹에 없다면 무조건 1등
else:
    print(1)
