import sys
input = sys.stdin.readline

# n: 점의 개수, m: 진행된 차례의 수
n, m = map(int, input().split())
play = [list(map(int, input().split())) for _ in range(m)]
parent = list(range(n+1))
answer = 0


def find_parent(x):
    # 값이 자기 자신이면 루트 정점
    if parent[x] == x:
        return x
    return find_parent(parent[x])


def union_parent(x, y):
    xp = find_parent(x)
    yp = find_parent(y)

    if xp == yp:
        return True

    if xp < yp:
        parent[yp] = xp
    else:
        parent[xp] = yp

    return False


for p in enumerate(play):
    idx, [a, b] = p

    # 사이클일 경우
    if union_parent(a, b):
        answer = idx + 1
        break


print(answer)
