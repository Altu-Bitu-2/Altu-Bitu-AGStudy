max_score = 0
max_list = []


def score_calculate(info, ryan):
    global max_score, max_list

    ryan_score = 0
    apeach_score = 0

    for i in range(11):
        # 둘 다 0점이면 계산하면 안 됨
        if info[i] == 0 and ryan[i] == 0:
            continue

        # 어피치가 더 많이 맞췄으면
        if info[i] >= ryan[i]:
            apeach_score += (10 - i)
        else:
            ryan_score += (10 - i)

    # 어피치와 라이언의 최대 점수 차 계산
    if ryan_score > apeach_score:
        diff = ryan_score - apeach_score
        if diff > max_score:
            max_score = diff
            max_list = list(ryan)

        elif diff == max_score:
            for i in range(10, -1, -1):
                if ryan[i] > max_list[i]:
                    max_list = list(ryan)
                    break
                elif ryan[i] < max_list[i]:
                    break


def dfs(n, info, idx, score):
    # 쏠 수 있는 화살이 남지 않았을 경우
    if n == 0:
        score_calculate(info, score)
        return

    # 인덱스 초과 시 리턴
    if idx == 11:
        return

    s = info[idx]

    # 어피치가 쏜 점수 + 1까지 계산
    for i in range(s + 2):
        # n을 넘지 않는 선에서 확인
        if n >= i:
            score[idx] = i
            dfs(n - i, info, idx + 1, score)
            # 방금 경우 제거하고 다음 경우 확인
            score[idx] = 0


def solution(n, info):
    dfs(n, info, 0, [0 for _ in range(11)])

    if not max_list:
        return [-1]
    else:
        return max_list