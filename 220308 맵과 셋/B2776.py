import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for i in range(m):
        # 값이 첫 번째 노트에 적혀 있는지 확인
        if note2[i] in note1:
            print(1)
        else:
            print(0)
