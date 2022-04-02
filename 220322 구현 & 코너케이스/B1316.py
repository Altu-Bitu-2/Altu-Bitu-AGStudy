n = int(input())

count = 0

for _ in range(n):
    word = input()

    word_list = []

    check = True
    for w in word:
        if w not in word_list:
            word_list.append(w)
        elif w == word_list[-1]:
            continue
        else:
            check = False
            break

    if check:
        count += 1

print(count)