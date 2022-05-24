# 반례 못 찾음

import sys
input = sys.stdin.readline

# 공백 제거해서 입력
string = input().rstrip()
answer = ''


# 자바 변수의 예외 처리
def java_to_c():
    result = True
    # 첫 글자가 대문자일 경우
    if string[0].isupper():
        result = False
    # 문자에 대문자도 소문자도 아닌 문자가 들어있을 때
    for s in string:
        if not s.isupper() and not s.islower():
            result = False
    return result


# C++ 변수의 예외 처리
def c_to_java():
    result = True
    # 언더바가 두개 있을 때
    if '__' in string:
        return False
    # 언더바가 처음과 끝에 붙어 있을 때
    if string[0] == '_' or string[-1] == '_':
        return False
    for s in string:
        # 대문자가 있을 때
        if s.isupper():
            return False
        # 소문자도 언더바도 아닌 문자가 들어 있을 때
        if not s.islower() and s != '_':
            return False
    return True


if '_' in string and c_to_java():
    under_bar = False
    for s in string:
        if s == '_':
            under_bar = True
        # 언더바가 있을 경우 다음 문자를 대문자로
        elif under_bar:
            under_bar = False
            answer += s.upper()
        else:
            answer += s
    print(answer)

elif '_' not in string and java_to_c():
    for s in string:
        # 대문자를 만나면 _ + 소문자로 변경
        if s.isupper():
            answer += '_' + s.lower()
        else:
            answer += s
    print(answer)

else:
    print("Error!")