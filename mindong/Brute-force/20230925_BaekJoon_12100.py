# 1. up, down, left, right
# 2. up은 맨위에 있는 것부터 
# 3. down은 맨 아래에 있는 것부터
# 4. left는 왼쪽에 있는 것부터
# 5. right 오른쪽에 있는 것부터

# 1. 하나씩 돌아가면서
# 0이면, continue
# 0이 아니면,
#     이전 위치의 값이 0이면, for문으로 벽이나 다를때까지 이동. 이때, 원래 인덱스 값 저장해놓음
#     이전 위치의 값이 다른숫자면, continue
#     이전 위치의 값이 같은 숫자면,
#         한번 합쳐진 것이면, continue
#         합쳐진 것이 아니면, n<<1, 그리고 0으로 대체



N = int(input())
cnt = []
for _ in range(N):
    cnt.append(list(map(int, input().split())))

def up(board):
    check = [[True]*N for _ in range(N)]
    for i in range(1, N):
        for j in range(0, N):
            if board[i][j] != 0:
                if board[i][j] == board[i-1][j] and check[i-1][j]:
                    board[i-1][j], board[i][j] = board[i-1][j] << 1, 0
                    check[i-1][j]=False
                    continue
                if board[i-1][j] == 0:
                    k = i-1
                    while 0<k<N-1 and board[k-1][j] == 0:
                        k -= 1  
                    if k == 0:
                        board[k][j], board[i][j] = board[i][j], 0
                    elif board[i][j] == board[k-1][j] and check[k-1][j]:
                        board[k-1][j], board[i][j] = board[k-1][j] << 1, 0
                        check[k-1][j]=False
                    else:
                        board[k][j], board[i][j] = board[i][j], 0  
    # for r in board:
    #     print(" ".join(list(map(str, r))))
    # print()
    return board

def down(board):
    check = [[True]*N for _ in range(N)]
    for i in range(N-2, -1, -1):
        for j in range(0, N):
            if board[i][j] != 0:
                if board[i][j] == board[i+1][j] and check[i+1][j]:
                    board[i+1][j], board[i][j] = board[i+1][j] << 1, 0
                    check[i+1][j]=False
                    continue
                if board[i+1][j] == 0:
                    k = i+1
                    while 0<k<N-1 and board[k+1][j] == 0:
                        k += 1
                    if k == N-1:
                        board[k][j], board[i][j] = board[i][j], 0
                    elif board[i][j] == board[k+1][j] and check[k+1][j]:
                        board[k+1][j], board[i][j] = board[k+1][j] << 1, 0
                        check[k+1][j]=False
                    else:
                        board[k][j], board[i][j] = board[i][j], 0
    # for r in board:
    #     print(" ".join(list(map(str, r))))
    # print()
    return board

def left(board):
    check = [[True]*N for _ in range(N)]
    for i in range(0, N):
        for j in range(1, N):
            if board[i][j] != 0:
                if board[i][j] == board[i][j-1] and check[i][j-1]:
                    board[i][j-1], board[i][j] = board[i][j-1] << 1, 0
                    check[i][j-1]=False
                    continue
                if board[i][j-1] == 0:
                    k = j-1
                    while 0<k<N-1 and board[i][k-1] == 0:
                        k -= 1
                    if k==0:
                        board[i][k], board[i][j] = board[i][j], 0
                    elif board[i][j] == board[i][k-1] and check[i][k-1]:
                        board[i][k-1], board[i][j] = board[i][k-1] << 1, 0
                        check[i][k-1]=False
                    else:   
                        board[i][k], board[i][j] = board[i][j], 0
    # for r in board:
    #     print(" ".join(list(map(str, r))))
    # print()
    return board

def right(board):
    check = [[True]*N for _ in range(N)]
    for i in range(0, N):
        for j in range(N-2, -1, -1):
            if board[i][j] != 0:
                if board[i][j] == board[i][j+1] and check[i][j+1]:
                    board[i][j+1], board[i][j] = board[i][j+1] << 1, 0
                    check[i][j+1]=False
                    continue
                if board[i][j+1] == 0:
                    k = j+1
                    while 0<k<N-1 and board[i][k+1] == 0:
                        k += 1
                    if k == N-1:
                        board[i][k], board[i][j] = board[i][j], 0
                    elif board[i][j] == board[i][k+1] and check[i][k+1]:
                        board[i][k+1], board[i][j] = board[i][k+1] << 1, 0
                        check[i][k+1]=False
                    else:
                        board[i][k], board[i][j] = board[i][j], 0   
    # for r in board:
    #     print(" ".join(list(map(str, r))))
    # print()
    return board

ans = 0
def go(num, cnt, dir):
    global ans
    if num > 4:
        max_value = 0
        for r in cnt:
            for value in r:
                if max_value < value:
                    max_value = value
        if ans < max_value:
            # print(dir)
            # for r in cnt:
            #     print(" ".join(list(map(str, r))))
            # print()  
            ans = max_value
        return
    go(num+1, up([row[:] for row in cnt]), dir+["up"])     
    go(num+1, down([row[:] for row in cnt]), dir+["down"])     
    go(num+1, left([row[:] for row in cnt]), dir+["left"])     
    go(num+1, right([row[:] for row in cnt]), dir+["right"])

go(0, cnt, [])

print(ans)