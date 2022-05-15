import sys
input = sys.stdin.readline

# 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# 같은 문자는 같은 개수만큼 있다.
n = int(input())

word = list(map(str, input().rstrip()))
array = [list(map(str, input().rstrip())) for _ in range(n-1)]

word.sort()
answer = 0

for arr in array:
    word_len = len(word)
    arr_len = len(arr)
    diff = 0

    # 정렬하기 전, 하나 차이난다면
    if arr_len == word_len:
        for i in range(word_len):
            if arr[i] != word[i]:
                diff += 1
        if diff == 1:
            answer += 1

    arr.sort()

    if arr_len == word_len and diff != 1:
        diff = 0
        # 정렬했을 때 두 문자열의 구성성분이 같거나 하나가 다르면
        for i in range(word_len):
            if arr[i] != word[i]:
                diff += 1
        if diff == 0 or diff == 1:
            answer += 1

    # 길이가 1 차이날 경우
    if abs(arr_len - word_len) == 1:
        # 더 긴 문자열을 한 글자씩 빼서 다른 문자열과 동일한지 확인
        if arr_len >= word_len:
            for i in range(arr_len):
                temp = arr[:i] + arr[i+1:]
                if temp == word:
                    answer += 1
                    break
        elif arr_len < word_len:
            for i in range(word_len):
                temp = word[:i] + word[i+1:]
                if temp == arr:
                    answer += 1
                    break


print(answer)
