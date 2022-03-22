from itertools import permutations
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input().split()))

permutation = list(permutations(list(range(1, 10)), 3))

answer = 0
for p in permutation:
    count = 0
    for j in range(n):
        strike = 0
        ball = 0
        for k in range(3):
            # strike와 ball의 개수 확인
            if str(p[k]) == arr[j][0][k]:
                strike += 1
            elif str(p[k]) in arr[j][0]:
                ball += 1
        # 주어진 개수와 동일하다면 카운트
        if strike == int(arr[j][1]) and ball == int(arr[j][2]):
            count += 1
    # 주어진 경우 모두 동일하다면 정답
    if count == n:
        answer += 1

print(answer)
