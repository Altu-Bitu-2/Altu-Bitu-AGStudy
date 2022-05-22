import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = []
number = []

while True:
    try:
        num = int(input())
        number.append(num)
    except:
        break


def post_order(start, end):

    if start > end:
        return

    root = number[start]

    # 루트보다 큰 값이 존재하지 않을 경우
    mid = end+1

    for idx in range(start+1, end+1):
        if number[idx] > root:
            mid = idx
            break

    # 중간 값 기준으로 왼쪽
    post_order(start+1, mid-1)

    # 중간 값 기준으로 오른쪽
    post_order(mid, end)

    print(number[start])


post_order(0, len(number)-1)

