n = int(input())

count = 0

for _ in range(n):
    word = input()

    word_list = set()
    before = None

    check = True
    for w in word:
        if w not in word_list:
            word_list.add(w)
        elif w == before:
            continue
        else:
            check = False
            break

        before = w

    if check:
        count += 1


print(count)
