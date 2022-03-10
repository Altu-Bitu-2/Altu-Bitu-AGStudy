
arr = list(range(1, 21))
sec = []

for i in range(10):
    a, b = map(int, input().split(' '))
    # 변경할 부분만 다른 배열에 저장해 역순으로 변환
    temp = arr[a-1:b]
    temp.reverse()
    # 원래 배열에 반영
    arr[a-1:b] = temp

for i in range(len(arr)):
    print(arr[i], end=' ')
