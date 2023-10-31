"""
1. S보다 작으면 end만 이동
    합계는 end를 더해가면서
2. S같으면 end-begin 값과 이전 최소값을 비교해서 갱신
     5번으로
3. S보다 크면 begin만 이동 합계는 begin를 빼면서 갱신
5. begin+1, end+1 로 세팅 후 다시 1-4 반복
"""
N, S = map(int, input().split())
li = list(map(int, input().split()))
ans = N+1
begin, end = 0, 0
value = sum(li[begin: end+1])

while begin < N:
    if value < S:
        end += 1
        if end == N:
            break
        value += li[end]
    elif value >= S:
        if end-begin+1 < ans:
            ans = end-begin+1
        value -= li[begin]
        begin += 1
if ans == N+1:
    print(0)
else:
    print(ans)

