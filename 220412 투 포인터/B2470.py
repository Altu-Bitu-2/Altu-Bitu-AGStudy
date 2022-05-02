import sys
input = sys.stdin.readline

# 산 => 1부터 1억까지
# 알칼리 => -1부터 -1억까지

# 특성 값이 0에 가장 가깝게

n = int(input())
s = list(map(int, input().split()))

s.sort()

left = 0
right = n - 1
answer = int(2e9)
solution_answer = [0, 0]

while left != right:
    result = s[left] + s[right]

    # 어떤 값이 0에 가까운지 비교
    if abs(result) < abs(answer):
        answer = result
        solution_answer[0] = s[left]
        solution_answer[1] = s[right]

    # 용액의 합이 0보다 작다면 왼쪽을 키워서 0에 가깝게 만들어 줌
    if result < 0:
        left += 1
    else:
        right -= 1

print(' '.join(map(str, solution_answer)))