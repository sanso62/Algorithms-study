n=int(input())
g_n=0
for num in range(1,n+1):
    square_root_n=int(num**0.5)
    for i in range(1, square_root_n+1):
        if num%i==0:
            if num==i**2:
                g_n+=i
            else:
                g_n+=i+num//i

print(g_n)

# 나머지 연산 정리로 변환해서 풀었으나 오히려 시간복잡도 커짐.
# 1000000을 인풋했을때, 60초 걸림.