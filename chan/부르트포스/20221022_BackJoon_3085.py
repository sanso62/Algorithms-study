# 3085번 - 사탕 게임

def find_first_max_candy (candy_map, max_candy):

    return max_candy

def find_max_candy (candy_map, row, col, max_candy):
    #가로 합

    #세로 합

    return max_candy

def change_map_col(candy_map, row, col):
    temp_candy = candy_map[row][col]
    candy_map[row][col] = candy_map[row][col + 1]
    candy_map[row][col + 1] = temp_candy
    print(candy_map)

def change_map_row(candy_map, row, col):
    temp_candy = candy_map[row][col]
    candy_map[row][col] = candy_map[row+1][col]
    candy_map[row+1][col] = temp_candy
    print(candy_map)


n = int(input())

# 빨간색 C / 파란색 P / 초록색 / Z / 노란색 Y
candy_map = []
for row in range(0,n):
    candy_arr = list(input())
    candy_map.append(candy_arr)
    print(candy_arr)

max_candy = -1
max_candy = find_first_max_candy(candy_map, max_candy)

for row in range(0,n):
    for col in range(0, n):
        #가로 값 바꾸기
        if(col + 1  < n):
            #오른쪽 값과 문자가 다를때만 교환
            if(candy_map[row][col] != candy_map[row][col+1]):
                # 가로 값 바꾸기
                change_map_col(candy_map,row, col)
                # max 값 업데이트
                find_max_candy (candy_map, row, col, max_candy)
                # 가로 값 원복
                change_map_col(candy_map, row, col)

        if (row + 1 < n):
            # 세로 값 바꾸기
            change_map_row(candy_map,row, col)
            # max 값 업데이트
            find_max_candy(candy_map, row, col, max_candy)
            # 세로 값 원복
            change_map_row(candy_map, row, col)