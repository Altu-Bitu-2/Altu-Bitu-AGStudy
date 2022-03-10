import sys

h, m, s = map(int, sys.stdin.readline().split())
sec = h * 3600 + m * 60 + s

q = sys.stdin.readline()

for _ in range(int(q)):
    inp = list(map(int, sys.stdin.readline().split()))

    if inp[0] == 3:
        # 만약 초가 0 이하가 되었다면 86,400을 더해 이전 날짜로 계산
        if sec < 0:
            sec += 86400

        # 초가 86,400이 넘을 경우
        sec %= 86400

        # 시, 분, 초 계산
        h = sec // 3600
        m = (sec % 3600) // 60
        s = (sec % 3600) % 60
        print(h, m, s)

    else:
        t = inp[0]
        c = inp[1]

        if t == 1:
            sec += c
        else:
            sec -= c
