import sys

start, fin, stream = sys.stdin.readline().split()

record = []

# 입력의 길이가 주어지지 않았으므로 입력이 끝나면 except를 발생시킴
while True:
    try:
        ts, name = sys.stdin.readline().split()
        record.append([ts, name])
    except:
        break

attend = set()
result = 0

for i in range(len(record)):
    # 시작 시간 이전에 채팅 기록이 있으면 set에 추가
    if record[i][0] <= start:
        attend.add(record[i][1])
    # 방송 종료 ~ 스트리밍 이전 사이에 기록이 있고 출석 기록이 있으면 count
    if fin <= record[i][0] <= stream and record[i][1] in attend:
        attend.remove(record[i][1])
        result += 1

print(result)
