n = list(input())
n.sort(reverse=True)

answer = -1

# 수에 0이 없거나 모두 다 더해서 3으로 나누어 떨어지지 않는 경우 => 30의 배수가 아님
if '0' not in n or sum(map(int, n)) % 3 != 0:
    print(answer)
else:
    print(''.join(n))
