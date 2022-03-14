n = int(input())

result = dict()

for _ in range(n):
    name, ext = input().split('.')

    # 확장자가 딕셔너리 내에 있는지 체크
    if ext not in result:
        result[ext] = 1
    else:
        result[ext] += 1

# 정렬을 위해 딕셔너리를 튜플-리스트로 변경
result = sorted(result.items())

for k in result:
    print(k[0], k[1])
