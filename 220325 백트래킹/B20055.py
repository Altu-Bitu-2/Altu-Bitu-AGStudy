# 길이가 N인 컨베이어 벨트

# '올리는 위치' 에 로봇을 올릴 수 있다.
# 로봇을 올릴 경우, 로봇이 이동한 칸은 내구도가 1이 감소한다.

# 1) 로봇과 함께 한 칸 회전
# 2) 한 칸 이동할 수 있다면 이동, 내구도가 남아 있어야 함
# 3) 내구도가 0이 아니면 로봇을 올린다.
# 4) 내구도가 0인 칸이 K개 이상일 경우 과정을 종료한다.
# 몇 단계가 진행 중일 때 종료 되었는지 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([False] * 2 * n)
step = 0

while True:
    # 벨트가 한 칸 회전
    a.appendleft(a.pop())


    # 로봇이 내리는 위치라면 내림
    robot.appendleft(robot.pop())

    if robot[n-1]:
        robot[n-1] = False

    # 로봇이 한 칸 이동 (할 수 있는지 없는지 여부 확인)
    for i in range(n, 0, -1):
        if robot[i]:
            # 다음 위치에 로봇이 없고, 내구도가 0이 아니며, i가 내리는 위치가 아니라면
            if not robot[i+1] and a[i+1] != 0:
                robot[i] = False
                robot[i+1] = True
                # 내구도 1 감소
                a[i+1] -= 1
        if robot[n-1]:
            robot[n-1] = False

    # 로봇 올림
    if a[0] != 0:
        robot[0] = True
        # 내구도 감소
        a[0] -= 1

    # 내구도 체크
    if a.count(0) >= k:
        break

    step += 1

print(step+1)