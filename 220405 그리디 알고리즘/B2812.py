import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().rstrip()))

stack = []

for i in range(n):
    # 가능한 앞쪽의 작은 수를 n개 삭제
    while stack and k > 0 and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(map(str, stack[:n-k])))
