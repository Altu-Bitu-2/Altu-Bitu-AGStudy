w, l, t = map(int, input().split())
d, l_d, a = map(int, input().split())

# 초기 일일 기초 대사량
not_intake = l
intake = l
not_w = w

for _ in range(d):
    # 소모 에너지 => 섭취 에너지 - (일일 기초 대사량 + 활동 대사량)
    energy = l_d - (intake + a)

    # 일일 기초 대사량이 변하지 않는 경우
    not_w += l_d - (not_intake + a)
    w += energy

    # abs(일일 에너지 섭취량 - 일일 에너지 소비량) > t
    if abs(energy) > t:
        intake += energy // 2


# 고려하지 않았을 때
if not_w <= 0:
    print("Danger Diet")
else:
    print(not_w, not_intake)

# 변화를 고려했을 때
if w <= 0 or intake <= 0:
    print("Danger Diet")
elif l - intake > 0:
    print(w, intake, "YOYO")
else:
    print(w, intake, "NO")