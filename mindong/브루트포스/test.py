# import sys
test_case=int(input())

min_t=501
def bf(a, l, t):
    global min_t
    for i in range(1, a+1):
        #a : 현재 타이어 수명
        #l : 현재 위치
        #t : 누적 교체시간
        #i : 없어지는 수명
        #a-i : 현재 타이어 수명 - 없어지는 수명
        #l+i : 현재 위치 + 없어지는 수명
        #t 교체 했나?
        if l+i>N:
            if t<min_t:
                min_t=t
        # t+=time[l+i] # 들리는 위치마다 해당되는 시간 업데이트
        # a=life[l+i] # 교체했을때, 수명 업데이트
        else:
            # print(a+life[l+i], l+i, t+time[l+i])?
            bf(life[l+i], l+i, t+time[l+i])
    
    
for i in range(test_case):
    N, F= map(int, input().split())
    life, time=[0], [0]
    for j in range(N):
        l, t =map(int, input().split())
        life.append(l)
        time.append(t)
    bf(F, 0, 0)
    print(min_t)
    
    