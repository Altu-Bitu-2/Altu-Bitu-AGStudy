import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 배열 정렬
arr.sort()
count = 0

for i in range(n):
    # 현재 탐색하는 값 제외
    tmp = arr[:i] + arr[i+1:]
    left = 0
    right = len(tmp) - 1
    while left != right:
        sum_value = tmp[left] + tmp[right]
        # 값의 합이 찾고자 하는 값과 같다면
        if sum_value == arr[i]:
            count += 1
            break
        # 값이 더 크면 오른쪽 수를 감소
        elif sum_value > arr[i]:
            right -= 1
        else:
            left += 1

print(count)