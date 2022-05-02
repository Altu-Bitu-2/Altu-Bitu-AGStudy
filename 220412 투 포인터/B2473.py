import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

s.sort()

# 최대 1억*3의 값까지 나올 수 있음
result = int(4e9)
answer = [0, 0, 0]

for i in range(n):
    left = 0
    right = n-1

    while left < i < right:
        # left, right가 i와 같으면 패스
        sum_value = s[left] + s[right] + s[i]
        # 0에 가까운 값 찾기
        if abs(result) > abs(sum_value):
            answer = [s[left], s[i], s[right]]
            result = sum_value

        if sum_value < 0:
            left += 1
        else:
            right -= 1

answer.sort()
print(' '.join(map(str, answer)))
