# 17427번 - 약수의 합 2

def f(num):
    temp_sum = 0
    for i in range(1, num+1):
        if (num % i == 0):
            temp_sum += i

    return temp_sum


def g(sum, num):
    sum += num

    return sum

max_num = int(input())

sum = 0
for i in range(1,max_num+1):
    num = f(i)
    sum = g(sum, num)

print (sum)

