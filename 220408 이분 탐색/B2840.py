import sys
input = sys.stdin.readline


def solution(wheel, idx):
    result = ['?'] * n

    # 역순으로 탐색 (마지막 문자열이 기준)
    for s, w in reversed(wheel):
        # 안에 다른 글자가 이미 있다면 보드판을 만들 수 없음
        if result[idx] != '?' and result[idx] != w:
            return '!'
        result[idx] = w

        if result.count(w) > 1:
            return '!'
        # 다음 회전할 횟수
        idx = (idx + int(s)) % n

    return ''.join(result)


# 바퀴의 칸의 수, 바퀴 돌리는 횟수
n, k = map(int, input().split())

# 몇 칸 이동했는지, 멈췄을 때 가리켰던 글자
wheel = [input().split() for _ in range(k)]
print(solution(wheel, 0))