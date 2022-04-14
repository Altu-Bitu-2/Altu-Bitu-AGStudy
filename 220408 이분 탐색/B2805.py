import sys
input = sys.stdin.readline


def binary_search(tree, m):
    start = 0
    end = max(tree)

    while start <= end:
        result = 0
        mid = (start + end) // 2
        for t in tree:
            if t - mid > 0:
                result += (t - mid)
        if result > m:
            start = mid + 1
        elif result < m:
            end = mid - 1
        else:
            return mid
        
    # 숫자를 정확히 맞출 수 없다면 1 작게 높이 설정해야 함
    return start - 1

# 절단기에 높이 H 지정

# 나무의 수, 나무의 길이
n, m = map(int, input().split())

# 나무의 높이
tree = list(map(int, input().split()))

# 7미터 가지고 가고 싶으면... 일단 H를 제일 높은 수로 설정해 max-1
# 그리고 1개씩 내려보는거야
# 20 => 0, 19 => 1... 16 => 3... 해서 7에 도달하면 스탑
# 자르고자 하는 목표치 보다 작으면 값을 내리고, 크면 값을 올림

print(binary_search(tree, m))
