# 2(x+y-2)개 => b
# xy-b => r

import math

r, b = map(int, input().split())

plus = b + r
for x in range(1, int(math.sqrt(plus))+1):
    y = plus / x
    if x + y == (r + 4) / 2:
        print(int(y), x)
        break
