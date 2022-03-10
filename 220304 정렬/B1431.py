n = int(input())

guitar = []

for _ in range(n):
    guitar.append(input())


def serial_sum(x):
    result = 0
    for k in x:
        # 숫자 여부 파악 후 계산
        if k.isdigit():
            result += int(k)
    # 결과 값을 기준으로 lambda를 이용해 정렬
    return result


guitar.sort(key=lambda x: (len(x), serial_sum(x), x))

for i in guitar:
    print(i)
