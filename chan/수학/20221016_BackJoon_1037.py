# 1037번 - 약수

cnt = int(input())
num_arr = list(map(int, input().split()))

num_arr.sort()

for target_value in range(1,1000001):
    find_value_flag = True
    for num in num_arr:
        if( target_value % num != 0 ):
            find_value_flag = False
            break

    if( find_value_flag ):
        if( target_value in num_arr ):
            print(target_value * num_arr[0])
            break
        else:
            print(target_value)
            break