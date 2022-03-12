
n = input()

result = set([])

# 1부터 문자열의 길이까지 숫자를 늘려가며 인덱싱
for i in range(len(n)):
    for j in range(len(n)-i):
        result.add(n[j:j+i+1])

print(len(result))
