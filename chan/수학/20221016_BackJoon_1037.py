# 1037번 - 약수

cnt = int(input())
num_arr = list(map(int, input().split()))

num_arr.sort()
if(cnt == 1):
    print(num_arr[0]*num_arr[0])
else:
    print(num_arr[0]*num_arr[cnt-1])