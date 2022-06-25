import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
plant = list(map(int, input().split()))
cost = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]
graph = []


def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])


def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return False

    # 둘 다 발전소에 연결되어 있다면 연결 안 함
    if px in plant and py in plant:
        return False

    # 발전소와 연결되어 있는 쪽으로 합치기
    if px in plant:
        parent[py] = px

    elif py in plant:
        parent[px] = py

    # 둘 다 발전소에 연결 안 되어 있다면 적은 쪽으로 합치기
    else:
        if px < py:
            parent[py] = px
        else:
            parent[px] = py

    return True


cost.sort(key=lambda x: x[2])

answer = 0

for c in cost:
    if union_parent(c[0], c[1]):
        answer += c[2]

print(answer)