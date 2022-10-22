# 2309번 - 일곱 난쟁이

def find_seven_height_sum_100(cur_index, cur_dwarf_cnt, height_sum, cur_height):
    visited[cur_index] = 1

    if( height_sum +  cur_height <= 100 ):
        height_sum = height_sum+ cur_height
    else:
        return height_sum

    if (cur_dwarf_cnt == 7):
        if (height_sum == 100):
            return height_sum

    for index in range (0,9):
        # 방문안한 곳만 들리기
        if (visited[index] == 0):
            height_sum = find_seven_height_sum_100(index, cur_dwarf_cnt+1, height_sum, height_arr[index])
            visited[index] = 0

# Main 시작
height_arr =[]
visited =[0,0,0,0,0,0,0,0,0]
# 9명의 키 입력
for i in range (1,10):
    height = int(input())
    height_arr.append(height)

for index in range (0,9):
    find_seven_height_sum_100(index,1,0,height_arr[index])

#print(height_arr)

# 9명 중에 7명 골라서 키의 합이 100인 경우 찾기
# 모든 조합의 경우의 수는 9! 팩토리얼




