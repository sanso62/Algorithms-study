# 2309번 - 일곱 난쟁이

def find_seven_height_sum_100(cur_dwarf_cnt, cur_index, height_sum):
    if (cur_dwarf_cnt == 7):
        if (height_sum == 100):
            return height_sum

    if (visited[cur_index] == 1):
        return height_sum



    for index in range (cur_index,9):
        temp_sum = height_sum + height_arr[index]
        find_seven_height_sum_100(cur_dwarf_cnt+1, index, temp_sum)

# Main 시작
height_arr =[]
visited =[0,0,0,0,0,0,0,0,0]
# 9명의 키 입력
for i in range (1,10):
    height = int(input())
    height_arr.append(height)

result = find_seven_height_sum_100(0,0,0)
print(result)

#print(height_arr)

# 9명 중에 7명 골라서 키의 합이 100인 경우 찾기
# 모든 조합의 경우의 수는 9! 팩토리얼




