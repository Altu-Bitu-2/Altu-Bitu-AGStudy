import math

n = int(input())

multiple = 1
divide = 1

arr = list(input().split())
prime = [0] * 100001


def factorization(k, op):
    if op == '*':
        for i in range(2, math.floor(math.sqrt(k))+1):
            while k % i == 0:
                k //= i
                prime[i] += 1
        if k > 1:
            prime[k] += 1
    else:
        for i in range(2, math.floor(math.sqrt(k))+1):
            while k % i == 0:
                k //= i
                prime[i] -= 1
        if k > 1:
            prime[k] -= 1


if '0' in arr:
    print("mint chocolate")

else:
    for i in range(2, len(arr), 2):
        number = abs(int(arr[i]))
        if arr[i-1] == '*':
            factorization(number, '*')
        elif arr[i-1] == '/':
            factorization(number, '/')

    check = 0

    for p in prime:
        if p < 0:
            check += 1
            break

    if check:
        print("toothpaste")
    else:
        print("mint chocolate")

