n, m = map(int, input().split(':'))

# 역순으로 두 수의 약수를 구함, 하나 구하는 순간 바로 break
for i in range(min(m, n), 0, -1):
    if m % i == 0 and n % i == 0:
        print(str(n // i) + ":" + str(m // i))
        break
