# 1748번 - 수 이어 쓰기 1

n = input()
int_n = int(n)

res = 0
for i in range(1,len(n)+1):
    odd = int_n%10

    if(odd == 0):
        res = res + (int_n % 10) * i
    res = res + (int_n%10) * i
    int_n = int_n // 10

print(res)