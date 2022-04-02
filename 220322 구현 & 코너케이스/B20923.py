from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

do = deque()
su = deque()

for _ in range(n):
    d, s = map(int, input().split())
    do.appendleft(d)
    su.appendleft(s)

do_ground = deque()
su_ground = deque()


def winner(result, winner, loser):
    # 승리했을 경우 상대 그라운드에서 값을 전부 가져오기

    while loser:
        result.appendleft(loser.popleft())

    while winner:
        result.appendleft(winner.popleft())

    return result


for i in range(m):

    if len(do) == 0 or len(su) == 0:
        break

    next_do = do.popleft()
    next_su = su.popleft()

    do_ground.append(next_do)
    su_ground.append(next_su)

    if next_do + next_su == 5:
        su = winner(su, su_ground, do_ground)
    elif next_do == 5 or next_su == 5:
        do = winner(do, do_ground, su_ground)
    else:
        # 아무도 안 가져갔을 경우 본인 그라운드에
        do_ground.append(next_do)
        su_ground.append(next_su)

if len(do) == len(su):
    print("dosu")
elif len(do) > len(su):
    print("do")
else:
    print("su")