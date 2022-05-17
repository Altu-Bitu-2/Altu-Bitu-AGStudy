import sys
from collections import Counter

input = sys.stdin.readline

SIZE = 26

"""
 [비슷한 단어]
 단어가 같은 구성일 조건
 1. 두 개의 단어가 같은 종류의 문자로 이루어짐
 2. 같은 문자는 같은 개수만큼 있음
 비슷한 단어의 조건
 1. 한 단어에서 한 문자를 더하거나, 빼면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 1개
 2. 한 단어에서 한 문자를 바꾸면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 2개
    -> !주의! 이때, 두 단어의 길이가 같아야 함 cf) doll | do
 <Counter>
 - iterable한 객체를 받아서 횟수를 기록하여 Counter 객체로 반환.
 - 이때 Counter 객체는 유사 dictionary라고 생각할 수 있다.
 - 주의할 점은, 일반 dictionary와는 다르게 default 값이 0으로 설정되어 있어, 삽입하지 않은 키 값에 대한 조회가 가능하다.
"""

# 입력
n = int(input())

source = input().rstrip()                   # 기준 문자열 받기
source_cnt = Counter(source)                # Counter: 단어에 포함된 알파벳의 글자를 세어주는 함수
ans = 0                                     # 초기 값 0

alphabets = [chr(i + ord('A')) for i in range(SIZE)]  # 알파벳 리스트

for _ in range(n - 1):                      # n-1번 반복
    target = input().rstrip()               # 공백 제거한 원하는 문자열
    diff = 0                                # 차이 개수
    target_cnt = Counter(target)            # 원하는 문자열의 알파벳 글자 세기

    for key in alphabets:                   # 알파벳 리스트 확인
        diff += abs(target_cnt[key] - source_cnt[key])  # Counter 객체이므로 키가 존재하는지 확인 불필요

    if diff <= 1 or (diff == 2 and len(target) == len(source)):     # 차이가 1개보다 작거나 같고, 차이가 2개일 경우 target과 source 문자열의 길이가 동일할 경우
        ans += 1                            # 유사 문자열 1개 추가

print(ans)                                  # 정답 출력