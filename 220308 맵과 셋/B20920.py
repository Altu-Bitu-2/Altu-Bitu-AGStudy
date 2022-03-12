n, m = map(int, input().split())

arr = dict()

for _ in range(n):
    word = input()

    # 단어의 길이 체크
    if len(word) < m:
        continue

    # 단어가 딕셔너리 내에 있는지 체크 후 개수 추가
    if word not in arr:
        arr[word] = 1
    else:
        arr[word] += 1

# 개수를 내림차순, 단어의 길이를 내림차순, 단어를 알파벳으로 정렬
arr = sorted(arr.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(arr)):
    print(arr[i][0])

