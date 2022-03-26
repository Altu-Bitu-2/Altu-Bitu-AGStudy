n, m = map(int, input().split())
card = list(map(int, input().split()))

answer = 0

card.sort()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            result = card[i] + card[j] + card[k]
            if result > m:
                break
            if answer < result:
                answer = result

print(answer)
