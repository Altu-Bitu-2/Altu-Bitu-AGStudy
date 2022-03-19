
# 유클리드 호제법으로 최대공약수
def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a


n, m = map(int, input().split())

# 최대공약수 * n => 최소공배수
k = m // n
value1 = 0
value2 = 0
answer = int(1e9)

for i in range(1, k//2+1):
    if k % i == 0:
        a = i
        b = k // i
        # 최대공약수가 1이 아니라면 패스
        if gcd(a, b) != 1:
            continue
        # 최소 조합 비교
        result = (a + b)
        if answer > result:
            answer = result
            value1 = a
            value2 = b

print(value1*n, value2*n)
