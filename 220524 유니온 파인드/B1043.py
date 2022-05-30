import sys
input = sys.stdin.readline

# n: 사람의 수, m: 파티의 수
n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
parties = []

parent = list(range(n+1))


def find_parent(x):
    # 값이 자기 자신이면 루트 정점
    if parent[x] == x:
        return x
    return find_parent(parent[x])


def union_parent(x, y):
    xp = find_parent(x)
    yp = find_parent(y)

    # 비밀을 아는 사람끼리는 묶이면 안 됨
    if xp in truth and yp in truth:
        return

    # 비밀을 아는 사람과 같은 그룹으로 묶기
    if xp in truth:
        parent[yp] = xp
    elif yp in truth:
        parent[xp] = yp
    else:
        if xp < yp:
            parent[yp] = xp
        else:
            parent[xp] = yp


for _ in range(m):
    party = list(map(int, input().split()))
    length = party[0]
    people = party[1:]

    for idx in range(length-1):
        union_parent(people[idx], people[idx+1])

    parties.append(people)

answer = 0

for party in parties:
    flag = True
    for i in range(len(party)):
        if find_parent(party[i]) in truth:
            flag = False
    if flag:
        answer += 1

print(answer)