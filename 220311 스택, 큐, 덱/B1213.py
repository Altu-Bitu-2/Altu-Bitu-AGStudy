arr = list(input())
arr.sort()

alphabet = dict()

# dict로 알파벳 개수 확인
for a in arr:
    if a not in alphabet:
        alphabet[a] = 1
    else:
        alphabet[a] += 1

odd = 0

for a in alphabet:
    # 홀수 개수와 홀수인 알파벳 확인
    if alphabet[a] % 2 != 0:
        odd += 1
        mid = a

result = []

# 각 알파벳 개수의 절반만큼 결과 배열에 append
for a in alphabet:
    for k in range(alphabet[a]//2):
        result.append(a)

# 만들어진 배열의 역순을 결과 배열의 뒤에 붙여 팰린드롬 생성
result += reversed(result)

# 만약 홀수인 값이 있다면 중간에 삽입
if odd != 0:
    result.insert(len(result)//2, mid)
answer = ''.join(result)

# 홀수가 1개 이상일 경우 팰린드롬을 만들 수 없으므로 Sorry.
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer)
