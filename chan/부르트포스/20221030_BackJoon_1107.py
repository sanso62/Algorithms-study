# 1107번 - 리모컨
# 리모컨 0~9 숫자, +, -
# + : +1, - : -1(0채널 -1은 응답없음)
# 고장난 버튼 개수 M
# 보고싶은 채널 N
# 없는 버튼을 선택할때 어떤 걸 누를것인지

def find_channel(tmp_N):
    global min_cnt, N, arr_btn

    for btn_num in arr_btn:
        if(btn_num != -1):
            tmp = tmp_N+ str(btn_num)

            cnt_gap = abs(int(N) - int(tmp))
            min_cnt = min(min_cnt, cnt_gap + len(tmp))

            if len(tmp) < 6:
                find_channel(tmp)


min_cnt = 999999

N = input()
M = int(input())
arr_btn = [0,1,2,3,4,5,6,7,8,9]
if( M > 0 ):
    broken_btn = map(int,input().split())
    for btn_num in broken_btn:
        arr_btn[btn_num] = -1

if N == '100':
    print(0)
    exit()


min_cnt = abs(int(N) - 100)

if M < 10:
    find_channel('')

print(min_cnt)