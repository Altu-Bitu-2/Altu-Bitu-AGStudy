n, m = map(int, input().split(':'))


def gcd(m, n):
    while n:
        mod = n
        n = m % n
        m = mod
    return m


divisor = gcd(m, n)

print("%d:%d" %(n // divisor, m // divisor))

