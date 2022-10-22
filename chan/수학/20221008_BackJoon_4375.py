# 4375번 - 1
# 10430 문제 자체의 규칙을 이해하는 것이 중요함.

while True:
    try:
        n = int(input())
    except:
        break

    mod = 0
    i = 1
    while True:
        mod = (mod*10) + 1
        mod = mod % n
        if mod == 0:
            print(i)
            break
        i = i + 1
