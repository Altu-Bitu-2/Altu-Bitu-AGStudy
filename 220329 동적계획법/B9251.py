import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())

d = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str1[j-1] == str2[i-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[-1][-1])