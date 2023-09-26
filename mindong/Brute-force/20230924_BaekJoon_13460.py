# 1. 같은 라인에 R과 O가 있으면 거의 끝난다고 보면 될듯
# 2. 끝점에서 끝점으로 이동만 가능
# 3. 같은 라인에 있는지 확인할때, 1씩 이동하면서 하면 될듯


# 동서남북 모두 브루트포스로 이동하는 방식 선택
# 1. 위, 오, 아래, 왼 순서로 
# 2. 파란색, 빨간색 비트마스크로 이동 .:1, #:0 으로 취급해서 #가 만날때까지 이동
# 3. O이 있으면, +1하고 리턴
# 4. 없으면, 1, 2, 3, 4 재귀로 반복

N, M = map(int, input().split())

rows, cols = ["0b" for _ in range(N)], ["0b" for _ in range(M)]
for i in range(N):
    li = list(input())
    for j,v in enumerate(li):
        if v == "#":
            rows[i]+="0"
            cols[j]+="0"
        elif v == ".":
            rows[i]+="1"
            cols[j]+="1"
        elif v == "O":
            rows[i]+="1"
            cols[j]+="1"
            hole = [i, j]
        elif v == "R":
            rows[i]+="1"
            cols[j]+="1"
            R = [i, j]
        elif v == "B":
            rows[i]+="1"
            cols[j]+="1"
            B = [i, j]

print(rows)
print(cols)

min_num = 11
def direct(red, blue, num):
    global min_num
    print("**",num)
    if num == 2:
        return
    if num > 10:
        return -1
    for dir in ["up", "down", "left", "right"]:
        if dir == "up":
            if red[1] == blue[1]:
                if red[0] > blue[0]:
                    print(1)
                    for n in range(N-1-(blue[0])+1, N):
                        if (int(cols[blue[1]], 2) & (1<<n)) == 0:
                            blue[0], prev_blue = N-n-1, blue
                            red[0], prev_red = N-n, red
                            break
                        else:
                            if (N-n-1, blue[1]) == hole:
                                return -1
                else:
                    print(2)
                    for n in range(N-1-(red[0])+1, N):
                        if (int(cols[red[1]], 2) & (1<<n)) == 0:
                            blue[0], prev_blue = N-n, blue
                            red[0], prev_red = N-n-1, red
                            break
                        else:
                            if (N-n-1, red[1]) == hole:
                                return num+1
            else:
                print(3)
                for n in range(N-1-(blue[0])+1, N):
                    if (int(cols[blue[1]], 2) & (1<<n)) == 0:
                        blue[0], prev_blue = N - n, blue
                        break
                    else:
                        if (N-n-1, blue[1]) == hole:
                            return -1
                for n in range(N-1-(red[0])+1, N):
                    if (int(cols[red[1]], 2) & (1<<n)) == 0:
                        red[0], prev_red = N - n, red
                        break
                    else:
                        if (N-n-1, red[1]) == hole:
                            return num+1
        elif dir=="down":
            if red[1] == blue[1]:
                if red[0] < blue[0]:
                    print(4)
                    for n in range(blue[0]+1, N):
                        if (int(cols[blue[1]], 2) & ((2**N)>>n)) == 0:
                            blue[0], prev_blue = n-1, blue
                            red[0], prev_red = n-2, red
                            break
                        else:
                            if (n, blue[1]) == hole:
                                return -1 
                else:
                    print(5)
                    for n in range(red[0]+1, N):
                        if (int(cols[red[1]], 2) & ((2**N)>>n)) == 0:
                            red[0], prev_red = n-1, red
                            blue[0], prev_blue = n-2, blue
                            break
                        else:
                            if (n, red[1]) == hole:
                                return num+1 
            else:
                print(6)
                for n in range(blue[0]+1, N):
                    if (int(cols[blue[1]], 2) & ((2**N)>>n)) == 0:
                        blue[0], prev_blue = n-1, blue
                        break
                    else:
                        if (n, blue[1]) == hole:
                            return -1
                for n in range(red[0]+1, N):
                    if (int(cols[red[1]], 2) & ((2**N)>>n)) == 0:
                        red[0], prev_red = n-1, red
                        break
                    else:
                        if (n, red[1]) == hole:
                            return num+1
        elif dir == "left":
            if red[0] == blue[0]:
                if red[1] > blue[1]:
                    print(7)
                    for m in range(M-1-(blue[1])+1, M):
                        if (int(rows[blue[0]], 2) & (1<<M)) == 0:
                            blue[1], prev_blue = M - m, blue
                            red[1], prev_red = M - m- 1, red
                            break
                        else:
                            if (blue[0], M-m-1) == hole:
                                return -1 
                else:
                    print(8)
                    for m in range(M-1-(red[1])+1, M):
                        if (int(rows[red[0]], 2) & (1<<m)) == 0:
                            red[1], prev_red = M - m, red
                            blue[1], prev_blue = M - m -1, blue
                            break
                        else:
                            if (red[0], M-m-1) == hole:
                                return num+1   
            else:
                print(9)
                for m in range(M-1-(blue[1])+1, M):
                    if (int(rows[blue[0]], 2) & (1<<m)) == 0:
                        blue[1], prev_blue = M - m, blue
                        break
                    else:
                        if (blue[0], M-m-1) == hole:
                            return -1
                for m in range(M-1-(red[1])+1, M):
                    if (int(rows[red[0]], 2) & (1<<m)) == 0:
                        red[1], prev_red = M - m, red
                        break
                    else:
                        if (red[0], M-m-1) == hole:
                            return num+1   
        elif dir=="right":
            if red[0] == blue[0]:
                if red[1] < blue[1]:
                    print(10)
                    for m in range(blue[1]+1, M):
                        if (int(rows[blue[0]], 2) & ((2**M)>>m)) == 0:
                            blue[1], prev_blue = m-1, blue
                            red[1], prev_red = m-2, red
                            break
                        else:
                            if (blue[0], m) == hole:
                                return -1
                else:
                    print(11)
                    for m in range(red[1]+1, M):
                        if (int(rows[red[0]], 2) & ((2**M)>>m)) == 0:
                            red[1], prev_red = m-1, red
                            blue[1], prev_blue = m-2, blue
                            break
                        else:
                            if (red[0], m) == hole:
                                return num+1   
            else:
                print(12)
                for m in range(blue[1]+1, M):
                    print("right")
                    print(int(rows[blue[0]], 2) & ((2**M)>>m))
                    return
                    if (int(rows[blue[0]], 2) & ((2**M)>>m)) == 0:
                        blue[1], prev_blue = m-1, blue
                        break
                    else:
                        if (blue[0], m) == hole:
                            return -1
                for m in range(red[1]+1, M):
                    if (int(rows[red[0]], 2) & ((2**M)>>m)) == 0:
                        red[1], prev_red = m-1, red
                        break
                    else:
                        if (red[0], m) == hole:
                            return num+1     
        result = direct(red, blue, num+1)
        if result and result < min_num:
            min_num = result
        blue = prev_blue
        red = prev_red              
            
direct(R, B, 0)
if min_num <= 10:
    print(min_num)
else:
    print(-1)






