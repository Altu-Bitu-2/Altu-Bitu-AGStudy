import sys
input = sys.stdin.readline

"""
 [과자 나눠주기]
 n개의 과자가 있을 때 m명의 조카에게 각각 같은 길이로 줄 수 있는 과자의 최대 길이를 구하는 문제
 -> 특정 과자 길이에 대하여 m명의 조카에게 나누어 줄 수 있는가?
 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
"""

# 내림차순 정렬된 snacks 리스트에서 length 길이의 과자를 몇개 만들 수 있는지 개수를 세어 리턴하는 함수
def split_snack(length, snacks):
    count = 0                               # 과자의 개수는 0
    for l in snacks:                        # 과자 길이 배열을 탐색
        if l < length:                      # 과자의 길이가 탐색할 길이보다 작으면
            return count                    # 현재 과자의 개수를 return
        count += l // length                # 아니라면 탐색할 길이 단위로 과자를 나눠 개수를 확인

    return count                            # 만들 수 있는 과자의 개수 return

def binary_search(m, snacks):
    left = 1                                # 시작을 1로
    right = snacks[0]                       # 가장 큰 수를 right
    while left <= right:                    # left가 right보다 커질 때까지 반복
        mid = (left + right) // 2           # left와 right의 중간 값을 mid로 설정
        if split_snack(mid, snacks) >= m:   # 나눌 수 있는 과자의 조각이 목표치보다 크면
            left = mid + 1                  # 목표값을 증가시켜서 재시도
        else:                               # 아니라면
            right = mid - 1                 # 목표값을 감소시켜서 재시도
    return left - 1                         # left - 1값을 return

m, n = map(int, input().split())            # 조카의 수 m, 과자의 수 n
snacks = list(map(int, input().split()))    # 과자 리스ㅌ로 받아오기
snacks.sort(reverse=True)                   # 내림차순 정렬

print(binary_search(m, snacks))             # 이진탐색 수행