import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 집의 개수, 연속된 집의 개수, 최소 돈의 양
    n, m, k = map(int, input().split())
    house = list(map(int, input().split()))

    # n == m이라면 훔칠 수 있는 경우의 수는 하나
    if m == n:
        if sum(house) < k:
            answer = 1
        else:
            answer = 0
    else:
        # 집 이어 붙이기
        house = house + house[:m-1]
        window = sum(house[:m])

        # 처음 집에서 훔칠 수 있는지 여부
        if window < k:
            answer = 1
        else:
            answer = 0

        for i in range(m, len(house)):
            window += house[i] - house[i - m]
            if window < k:
                answer += 1

    print(answer)
