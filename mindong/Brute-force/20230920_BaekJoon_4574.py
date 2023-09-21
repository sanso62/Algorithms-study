digit = {"A": 1, "B": 2, "C": 3,
         "D": 4, "E": 5, "F": 6,
         "G": 7, "H": 8, "I": 9 }

def check1(x, y, cur_cnt):
    s = set()
    for v in cur_cnt[y]:
        if v!=0:
            s.add(v)
    for r in range(9):
        if cur_cnt[r][x] !=0:
            s.add(cur_cnt[r][x])
    for i in [(y//3)*3, (y//3)*3+1, (y//3)*3+2]:
        for j in [(x//3)*3, (x//3)*3+1, (x//3)*3+2]:
            if cur_cnt[i][j]!=0:
                s.add(cur_cnt[i][j])
    values = []
    for v in range(1, 10):
        if v not in s:
            values.append(v)
    return values

def check2(x, y, cur_cnt, val):
    if val in cur_cnt[y]:
        return False
    for r in range(9):
        if val == cur_cnt[r][x]:
            return False
    for i in [(y//3)*3, (y//3)*3+1, (y//3)*3+2]:
        for j in [(x//3)*3, (x//3)*3+1, (x//3)*3+2]:
            if val == cur_cnt[i][j]:
                return False

    return True

def go(x, y, cur_cnt, cur_uv):
    global result
    # print(x, y)
    if y == 9:
        # print("y==9")
        result = []
        # for row in cur_cnt:
        #     print("".join(list(map(str, row))))
        for row in cur_cnt:
            result.append("".join(list(map(str, row))))
        return
    if cur_cnt[y][x] == 0:
        # print("cur_cnt[y][x] == 0")
        possible_values = check1(x, y, cur_cnt)
        # print(possible_values)
        for v1 in possible_values:
            cur_cnt[y][x] = v1
            for v2 in range(1, 10):
                if cur_uv[v1][v2]:
                    continue
                cur_uv[v1][v2], cur_uv[v2][v1] = True, True
                if x+1<9 and cur_cnt[y][x+1] == 0 and check2(x+1, y, cur_cnt, v2):
                    cur_cnt[y][x+1] = v2
                    if x+1 < 9:
                        go(x+1, y, cur_cnt, cur_uv)
                    else:
                        go(0, y+1, cur_cnt, cur_uv)
                    if result:
                        return
                    cur_cnt[y][x+1] = 0
                if y+1<9 and cur_cnt[y+1][x] == 0 and check2(x, y+1, cur_cnt, v2):
                    cur_cnt[y+1][x] = v2
                    if x+1 < 9:
                        go(x+1, y, cur_cnt, cur_uv)
                    else:
                        go(0, y+1, cur_cnt, cur_uv)
                    if result:
                        return
                    cur_cnt[y+1][x] = 0        
                cur_uv[v1][v2], cur_uv[v2][v1] = False, False
            
            cur_cnt[y][x] = 0
        return        
    else:
        if x+1 < 9:
            go(x+1, y, cur_cnt, cur_uv)
        else:
            go(0, y+1, cur_cnt, cur_uv)

num, results = 1, []
while True:
    n = int(input())
    if n<=0:
        break
    cnt = [[0 for _ in range(9)] for _ in range(9)]
    uv = [[False for _ in range(10)] for _ in range(10)]
    for _ in range(n):
        u, lu, v, lv = input().split()
        cnt[digit[lu[0]]-1][int(lu[1])-1] = int(u)
        cnt[digit[lv[0]]-1][int(lv[1])-1] = int(v)      
        uv[int(u)][int(v)] = True
        uv[int(v)][int(u)] = True
    
    ln = input().split()
    for i, l in enumerate(ln):
        cnt[digit[l[0]]-1][int(l[1])-1] = i+1
    
    # for row in cnt:
    #     print("".join(list(map(str, row))))
    result = False
    go(0, 0, cnt, uv)
    results.append(f"Puzzle {num}")
    for row in result:
        results.append(row)
    num+=1

for res in results:
    print(res)

"""
왼쪽에서 오른쪽
위에서 아래순

1. 행 check
2. 열 check
3. 3x3 check
가능한 숫자 list
4. 가능한 숫자 조합 check
오른쪽으로 연결 or 아래쪽으로 연결
5. 행 check
6. 열 check
7. 3x3 check
"""