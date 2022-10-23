# 1978번 - 소수 찾기

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

cnt = int(input())
num_arr = list(map(int, input().split()))
ans = 0
for num in num_arr:
    if is_prime(num):
        ans += 1

print(ans)