import sys
input = sys.stdin.readline

n = int(input())
node = list(map(int, input().split()))
leaf = [True for _ in range(n)]

# 지울 노드
d = int(input())


def find_parent(s, num, step):
    # 한 계단 이상 올라와 발견된 노드 => 리프 노드가 아님
    if step > 0:
        leaf[num] = False

    # 최상단 노드가 루트이면 반환
    if node[num] == -1:
        return
    # 최상단 노드가 -2라면 삭제된 노드
    if node[num] == -2:
        node[s] = -2
    else:
        # 부모 탐색
        find_parent(s, node[num], step + 1)


# 삭제한 노드 -2로
node[d] = -2

for idx in range(len(node)):
    find_parent(idx, idx, 0)

count = 0

# 리프 노드이며 삭제되지 않은 노드 카운트
for idx in range(len(node)):
    if leaf[idx] and node[idx] != -2:
        count += 1

print(count)
