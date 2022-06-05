def rule(answer):
    # check rule

    for x, y, s in answer:
        # 기둥일 경우
        if s == 0:
            # 바닥에 세워질 경우
            if y == 0:
                continue
            # 기둥이 보의 한쪽 끝 위에 있을 경우
            elif (x-1, y, 1) in answer or (x, y, 1) in answer:
                continue
            # 기둥이 기둥 위에 있을 경우
            elif (x, y-1, 0) in answer:
                continue
            else:
                return False

        # 보일 경우
        if s == 1:
            # 보가 기둥에 연결 되어 있을 경우
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer:
                continue
            # 양 옆에 보가 연결되어 있을 경우
            elif (x+1, y, 1) in answer and (x-1, y, 1) in answer:
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = set()

    for i in range(len(build_frame)):
        x = build_frame[i][0]
        y = build_frame[i][1]
        a = build_frame[i][2]
        b = build_frame[i][3]

        if b == 1:
            answer.add((x, y, a))
            if not rule(answer):
                answer.remove((x, y, a))

        if b == 0:
            answer.remove((x, y, a))
            if not rule(answer):
                answer.add((x, y, a))

    answer = [list(ans) for ans in answer]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer