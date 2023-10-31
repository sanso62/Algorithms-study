"""
이전에 구한 값을 재사용
1 2 3 4 2 5 3 1 1 2
1 2 3 > 5 -> 합한것에서 1부터 빼면서 구해보기
  2 3 = 5 -> 멈추고 3부터 시작, ans+1
--------
    3 4 > 5 -> 합한것에서 3부터 빼면서 구해보기
      4 < 5 -> 멈추고 4부터 시작
      4 2 > 
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
begin, end = 0, 0
value = sum(A[begin: end+1])
while begin < N :
    # print ("*", begin, end)
    if value < M:
        end += 1
        if end == N:
            break
        value += A[end]
    elif value > M:
        value -= A[begin]
        begin += 1
    elif value == M:
        ans += 1
        value -= A[begin]
        begin += 1
        end += 1
        if end == N:
            break
        value += A[end]
        
print(ans)