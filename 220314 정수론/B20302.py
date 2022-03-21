import math

n = int(input())
arr = list(input().split())

prime_number = [[] for _ in range(100001)]
prime_check = [True] * 100001
cal = [0] * 100001


def prime(n):
    prime_number[1].append(1)
    for i in range(2, n+1):
        if prime_check[i]:
            j = 2
            prime_number[i].append(i)
            # i랑 j를 곱한 수를 전부 False로 (소수가 아니므로)
            while i * j <= n:
                prime_check[i*j] = False
                prime_number[i*j] = prime_number[i] + prime_number[j]
                j += 1


# 입력된 최대 수만큼 에라토스테네스의 체로 소수 여부 배열에 저장
prime(100000)

def factorization(nb, op):
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

    for p in cal:
        if p < 0:
            check += 1
            break

    if check:
        print("toothpaste")
    else:
        print("mint chocolate")

