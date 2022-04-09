import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def matrix_check(matrix_a, matrix_b):
    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True


matrix_a = []
matrix_b = []
answer = 0

for _ in range(n):
    matrix_a.append(list(map(int, input().rstrip())))

for _ in range(n):
    matrix_b.append(list(map(int, input().rstrip())))

# 3 x 3 배열 이상 일 때 연산 가능
if n > 2 or m > 2:
    for i in range(n):
        for j in range(m):
            # a와 b 행렬 값이 다르다면
            if matrix_a[i][j] != matrix_b[i][j]:
                # 3 x 3 영역 밖에서 수가 다르면 만들 방법이 없음
                if i >= n - 2 or j >= m - 2:
                    answer = -1
                    break
                # 3 x 3 영역 flip
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        matrix_a[x][y] = int(not matrix_a[x][y])
                answer += 1

# 마지막에 행렬이 동일한지 체크
if not matrix_check(matrix_a, matrix_b):
    answer = -1

print(answer)
