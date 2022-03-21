import math

n = int(input())
arr = list(input().split())

prime_number = [[] for _ in range(100001)]
prime_check = [True] * 100001
cal = [0] * 100001


def prime(n):
    prime_number[1].append(1)
    for i in range(2, n+1):
        # 소수 여부 체크
        if prime_check[i]:
            j = 2
            prime_number[i].append(i)
            while i * j <= n:
                prime_check[i*j] = False
                # i의 배수가 되는 수를 찾아 각 소수의 리스트를 더함
                prime_number[i*j] = prime_number[i] + prime_number[j]
                j += 1


# 입력된 최대 수만큼 에라토스테네스의 체로 소수 여부 배열에 저장
prime(100000)


def factorization(nb, op):
    # 곱일 경우 해당 수의 소수를 +, 아니라면 -.
    if op == '*':
        for r in prime_number[nb]:
            cal[r] += 1
    else:
        for r in prime_number[nb]:
            cal[r] -= 1


if '0' in arr:
    print("mint chocolate")

else:
    for i in range(0, len(arr)+1, 2):
        number = abs(int(arr[i]))
        if i == 0: factorization(number, '*')
        else: factorization(number, arr[i-1])

    check = 0

    # 음수가 하나라도 있으면 유리수

    for i in range(2, len(cal)):
        if cal[i] < 0:
            check += 1
            break

    if check:
        print("toothpaste")
    else:
        print("mint chocolate")

