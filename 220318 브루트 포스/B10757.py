def calculator(a, b, carry):
    temp = [0] * len(a)

    for i in range(len(b)):
        result = a[i] + b[i] + carry
        temp[i] = result % 10
        # carry를 합한 값이 10이 넘어가면 carry = 1
        if result >= 10:
            carry = 1
        else:
            carry = 0

    for i in range(len(b), len(a)):
        result = a[i] + carry
        temp[i] = result % 10
        # carry를 합한 값이 10이 넘어가면 carry = 1
        if result >= 10:
            carry = 1
        else:
            carry = 0

    if carry == 1:
        temp += [1]

    # 남은 carry 값도 함께 return
    return temp


def solution():
    a, b = input().split()

    a = list(map(int, a))
    b = list(map(int, b))

    # 배열을 역순으로 변경
    a.reverse()
    b.reverse()

    # 길이가 긴 것을 앞에 위치
    if len(b) > len(a):
        a, b = b, a

    # 짧은 영역 길이만큼 계산
    result = calculator(a, b, 0)

    # 다시 역순으로 변경
    result.reverse()

    print(''.join(map(str, result)))

solution()