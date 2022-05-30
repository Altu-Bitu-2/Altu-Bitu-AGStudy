import sys
import math
input = sys.stdin.readline

x, n = map(int, input().split())

if n != 1 and n % 2 != 0:
    print("ERROR")

elif (n == 0 and x > 0) or (n == 1 and x < 0):
    print("INFINITE")

elif x > 0 and n != 0 and n % 2 == 0:
    print(math.ceil(x / (n/2)) - 1)

else:
    print("0")
