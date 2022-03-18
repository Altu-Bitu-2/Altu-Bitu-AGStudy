import sys

input = sys.stdin.readline

n, p = map(int, input().split())

stack = [[] for _ in range(n)]
answer = 0

for _ in range(n):
    line, flat = map(int, input().split())

    while True:
        # 플랫이 스택에 없으면 추가 (누름)
        if not stack[line]:
            answer += 1
            stack[line].append(flat)
        else:
            # 플랫이 가장 마지막으로 누른 플랫보다 작다면 제거 (손 떼기)
            if stack[line][-1] > flat:
                answer += 1
                stack[line].pop()
            elif stack[line][-1] < flat:
                answer += 1
                stack[line].append(flat)
                break
            else:
                break

print(answer)