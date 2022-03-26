t = int(input())

number = [[] for _ in range(10)]
number[0].append(10)

for _ in range(t):
    a, b = map(int, input().split())
    # 일의 자리만 남김
    a %= 10
    k = a

    # 일의 자리만 계산 => 제곱수면 일의 자리가 반복된다.
    while k not in number[a] and a != 0:
        number[a].append(k)
        k = k * a % 10

    print(number[a][b % len(number[a])-1])
