"""
1. 소수 판별: 제곱근까지 일일히 확인하는 방식
2. dp 로 풀어야 할듯. 1부터 시작해서 소수의 합만 
   저장하면서

2 3 5 7
  5

2
2 3 5
2 3 5 5 8 10
2 3 5 5 8 10 7 12 15 17
2 3 5 5 8 10 7 12 15 17 11 18 23 26 28
13 24 31 36 39 41
17 30 41 48 53 56 58
19 36 49 
23 
앞의 뒤에서 n번째 숫자부터 더해서 저장해놓는 방식

------ 이 방식으로 하면 시간초과

방법2
소수를 일단 다구하고 투포인터로 이동하면서 확인
2 3 5 7 11 13   13
2
2 3
2 3 5
2 3 5 7
  3 5 7
    5 7
    5 7 11
      7 11
        11
        11 13
           13

1 2 3 4 5 6 7 41
"""
N = int(input())
ans = 0

def is_prime(num):
    for n in range(2, int(num**0.5)+2):
        if num % n == 0:
            return False
    return True

li = [2]
for num in range(2, N+1):
    if is_prime(num):
        li.append(num)
len_li = len(li)
# print(li)
begin, end = 0, 0
value = sum(li[begin:end+1])
while N > 1 and begin <= len_li:
    if value < N:
        end+=1
        if end == len_li:
            break
        value+=li[end]
    elif value == N:
        ans+=1
        value -= li[begin]
        begin += 1
        end += 1
        if end == len_li:
            break
        value+=li[end]
    elif value > N or end == len_li-1:
        value -= li[begin]
        begin += 1
print(ans)
