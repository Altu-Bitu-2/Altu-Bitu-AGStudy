def calculator(end, a, b, carry):
    temp = [0] * end

    for i in range(end):
        result = a[i] + b[i] + carry
        temp[i] = result % 10
        # carry를 합한 값이 10이 넘어가면 carry = 1
        if result >= 10:
            carry = 1
        else:
            carry = 0

    # 남은 carry 값도 함께 return
    return temp, carry


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

    length = len(a) - len(b)

    # 짧은 영역 길이만큼 계산
    result, carry = calculator(len(b), a[0:len(b)], b, 0)
    # 남은 길이 영역의 덧셈 계산
    result2, carry2 = calculator(length, a[len(b):], [0] * length, carry)
    answer = result + result2

    # 마지막에 carry 값이 나올 경우 올림수 추가
    if carry2 == 1:
        answer += [1]

    # 다시 역순으로 변경
    answer.reverse()

    print(''.join(map(str, answer)))

solution()