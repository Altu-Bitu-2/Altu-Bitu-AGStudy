import math

num = []

while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)

n = max(num)

arr = [True for i in range(n+1)]

# 에라토스테네스의 체
def prime(n):

    for i in range(2, int(math.sqrt(n))+1):
        # 숫자가 참일 경우
        if arr[i]:
            j = 2
            # i랑 j를 곱한 수를 전부 False로 (소수가 아니므로)
            while i * j <= n:
                arr[i*j] = False
                j += 1

# 입력된 최대 수만큼 에라토스테네스의 체로 소수 여부 배열에 저장
prime(n)

for n in num:
    for i in range(2, n//2+1):
        a = i
        b = n - i
        # a와 b 모두 소수라면
        if arr[a] and arr[b]:
            print("%d = %d + %d" %(n, a, b))
            break
        # 마지막까지 소수 조합을 찾지 못했다면
        if i == n//2:
            print("Goldbach's conjecture is wrong.")