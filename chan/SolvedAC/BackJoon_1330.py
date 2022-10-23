# 1330번 - 두 수 비교하기

a,b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')