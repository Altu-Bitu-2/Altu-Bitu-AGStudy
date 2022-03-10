
n = int(input())

arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

# 팁을 가능한 많이 받기 위해 역순으로 정렬
arr.sort(reverse=True)

for i in range(len(arr)):
    # 음수일 경우 팁은 받지 못함
    if arr[i] - i <= 0:
        continue
    else:
        result += arr[i] - i

print(result)