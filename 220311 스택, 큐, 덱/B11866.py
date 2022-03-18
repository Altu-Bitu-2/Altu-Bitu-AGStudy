n, k = map(int, input().split())

arr = list(range(1, n+1))
result = []

num = 0

for i in range(1, n+1):
    num += k-1
    if num >= len(arr):
        num = num % len(arr)
    result.append(arr.pop(num))

print('<', end='')
for i in range(n-1):
    print("%d, " %result[i], end='')
print(result[-1], end='')
print('>')
