t = int(input())

for _ in range(t):

    n = int(input())
    result = dict()

    for _ in range(n):
        # 옷 이름, 종류를 input
        cloth, kind = input().split()

        # 옷 종류가 딕셔너리에 존재하는지 여부를 판단해 종류 별 개수 체크
        if kind not in result:
            result[kind] = 1
        else:
            result[kind] += 1

    answer = 1

    # 종류 별로 옷을 입을 수 있는 경우의 수 확인
    for key in result.keys():
        answer *= int(result[key]) + 1

    print(answer - 1)
