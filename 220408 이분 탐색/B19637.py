import sys
input = sys.stdin.readline


def binary_search(power, grade):
    start = 0
    end = len(grade) - 1

    while start <= end:
        mid = (start + end) // 2
        value = int(grade[mid][1])
        # 찾는 값이 작다면
        if power < value:
            end = mid - 1
        elif power > value:
            start = mid + 1
        else:
            # 동일한 값이 여러 개라면 더 앞의 값 출력
            if mid != 0 and int(grade[mid-1][1]) == power:
                end = mid
            else:
                return grade[mid][0]

    return grade[start][0]


# 칭호의 개수, 칭호를 출력해야 하는 캐릭터의 개수
n, m = map(int, input().split())

# 칭호의 이름 (1~11) <- 전투력 상한 오름차순
grade = [input().split() for _ in range(n)]

# 전투력
for _ in range(m):
    print(binary_search(int(input()), grade))