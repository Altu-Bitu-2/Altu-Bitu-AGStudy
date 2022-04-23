import sys
input = sys.stdin.readline


def binary_search(tree, m):
    start = 0
    end = tree[0]

    while start <= end:
        result = 0
        mid = (start + end) // 2
        for t in tree:
            if t <= mid:
                break
            result += (t - mid)
        if result >= m:
            start = mid + 1
        elif result < m:
            end = mid - 1
        
    # 숫자를 정확히 맞출 수 없다면 1 작게 높이 설정해야 함
    return start - 1

# 나무의 수, 나무의 길이
n, m = map(int, input().split())

# 나무의 높이
tree = list(map(int, input().split()))
tree.sort(reverse=True)
print(binary_search(tree, m))
