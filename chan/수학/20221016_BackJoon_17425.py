#17425번 - 약수의 합
def f(num):
    temp_sum = 0
    for i in range(1, num+1):
        if (num % i == 0):
            temp_sum += i

    return temp_sum


def g(sum, num):
    sum += num

    return sum

def print_result():
    max_num = int(input())

    sum = 0
    for i in range(1,max_num+1):
        num = f(i)
        sum = g(sum, num)

    print (sum)

cnt = int (input())

for i in range(0,cnt):
    print_result()
