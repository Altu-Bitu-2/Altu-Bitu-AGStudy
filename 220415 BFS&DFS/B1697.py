import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001

def bfs(cur, step):
    queue = deque([(cur, step)])
    answer = int(1e9)

    while queue:
        c, s = queue.popleft()
        # 현재 위치가 동생의 위치와 같다면
        if c == k and answer > s:
            answer = s
        # BFS로 모든 경우 탐색
        if not visited[c] and s < answer:
            visited[c] = True
            if c < 100000:
                queue.append((c + 1, s + 1))
            if c > 0:
                queue.append((c - 1, s + 1))
            if c <= 50000:
                queue.append((c * 2, s + 1))

    return answer


print(bfs(n, 0))