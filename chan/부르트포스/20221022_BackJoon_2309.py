# 2309번 - 일곱 난쟁이

height_arr =[]
total_height_sum = 0
# 9명의 키 입력
for i in range (1,10):
    height = int(input())
    height_arr.append(height)
    total_height_sum = total_height_sum + height

#print(height_arr)

height_arr.sort()

# 9명 중에 7명 골라서 키의 합이 100인 경우 찾기
# 9명중 7명 고르는건 9명 중 2명 고르는 것과 같음
stop_flag = False
for i in range (0,9):
    if(stop_flag):
        break
    for j in range (i,9):
        if (i==j):
            continue

        temp_sum = total_height_sum - height_arr[i] - height_arr[j]
        if(temp_sum == 100):
            height_arr[i] = 0
            height_arr[j] = 0
            stop_flag = True

        if (stop_flag):
            break

for height in height_arr:
    if(height != 0):
        print(height)



