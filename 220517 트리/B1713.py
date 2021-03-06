import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

recommend = list(map(int, input().split()))

dict_photo = {}

for rec in enumerate(recommend):
    idx, r = rec

    # 사진틀이 비었다면
    if not dict_photo:
        dict_photo[r] = [0, idx]

    # 사진틀에 사진이 있다면 추천 수 증가
    elif r in dict_photo:
        dict_photo[r][0] += 1
    else:
        if len(dict_photo) == n:
            delete = sorted(dict_photo.items(), key=lambda x: (x[1][0], x[1][1]))
            del dict_photo[delete[0][0]]
        dict_photo[r] = [0, idx]

print(*sorted(dict_photo.keys()))