n = int(input())

multiple = 1
divide = 1

arr = list(input().split())

if '0' in arr:
    print("mint chocolate")

else:
    for i in range(2, len(arr)):
        if arr[i-1] == '*':
            multiple *= int(arr[i])
        elif arr[i-1] == '/':
            divide *= int(arr[i])

    if multiple % divide == 0:
        print("mint chocolate")
    else:
        print("toothpaste")
