# 2475번 - 검증수

num_arr = map(int, input().split())

sum = 0
for num in num_arr:
    sum = sum + (num*num)%10
    sum = sum%10

print(sum)