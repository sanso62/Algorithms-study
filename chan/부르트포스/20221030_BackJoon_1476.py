# 1476번 - 날짜 계산
# 지구 E , 태양 S, 달 M 연도 표시
# (1<= E <= 15, 1<= S <= 28, 1<= M <= 19)

E, S ,M = map(int, input().split())

year = 1
tmp_E = 1
tmp_S = 1
tmp_M = 1

while True:
    if(tmp_E== E and tmp_S ==S and tmp_M == M):
        print(year)
        break

    tmp_E += 1
    tmp_S += 1
    tmp_M += 1
    year += 1

    if(tmp_E > 15):
        tmp_E = 1
    if(tmp_S > 28):
        tmp_S = 1
    if(tmp_M > 19):
        tmp_M = 1

