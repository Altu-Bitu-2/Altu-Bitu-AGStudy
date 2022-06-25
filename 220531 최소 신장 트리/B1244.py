import sys
input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))
m = int(input())
number = [list(map(int, input().split())) for _ in range(m)]


def boy_switch(s):
    for i in range(s, len(switch), s):
        switch[i] = not switch[i]


def girl_switch(s):
    left, right = s-1, s+1
    switch[s] = not switch[s]

    while left >= 0 and right < len(switch):
        if switch[left] == switch[right]:
            switch[left] = not switch[left]
            switch[right] = not switch[right]
            left -= 1
            right += 1
        else:
            break


for num in number:
    gender, s = num

    if gender == 1:
        boy_switch(s)
    else:
        girl_switch(s)


switch = list(map(int, switch))
for k in range(1, len(switch), 20):
    print(*switch[k:k+20])
