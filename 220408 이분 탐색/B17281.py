import sys
from itertools import permutations
input = sys.stdin.readline

# 이닝 수, 이닝에서 얻는 결과
n = int(input())
# 안타 1, 2루타 2, 3루타 3, 홈런 4, 아웃 0
inning = [list(map(int, input().split())) for _ in range(n)]


def cal_score(perm):
    idx = 0
    score = 0
    for i in range(n):
        out = 0
        b1, b2, b3 = 0, 0, 0
        # 점수 계산. 아웃이 3번보다 적을 경우에 반복, 아니라면 이닝 종료
        while out < 3:
            cur = perm[idx % 9]
            # 안타
            if inning[i][cur] == 0:
                out += 1
            elif inning[i][cur] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[i][cur] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[i][cur] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif inning[i][cur] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx += 1

    return score


answer = 0
hitter = list(range(1, 9))

# 모든 경우의 수 계산
for perm in permutations(hitter):
    perm = list(perm[:3]) + [0] + list(perm[3:])
    answer = max(cal_score(perm), answer)

print(answer)
