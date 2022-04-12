import sys
input = sys.stdin.readline


def matrix_check(matrix_a, matrix_b):
    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True


n, m = map(int, input().split())
matrix_a = [list(map(int, input().rstrip())) for _ in range(n)]
matrix_b = [list(map(int, input().rstrip())) for _ in range(n)]

answer = 0

# 3 x 3 배열 이상일 때 연산 가능
if n > 2 or m > 2:
    for i in range(n-2):
        for j in range(m-2):
            # a와 b 행렬 값이 다르다면
            if matrix_a[i][j] != matrix_b[i][j]:
                # 3 x 3 영역 flip
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        matrix_a[x][y] = int(not matrix_a[x][y])
                answer += 1

# 마지막에 행렬이 동일한지 체크
if not matrix_check(matrix_a, matrix_b):
    answer = -1

print(answer)
