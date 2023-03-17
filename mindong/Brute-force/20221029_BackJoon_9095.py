import sys

test_case=sys.stdin.read().splitlines()

sums=[1, 2, 4]
for i in range(4,11):
    three=i-3
    two=i-2
    one=i-1
    sums.append(sums[three-1]+sums[two-1]+sums[one-1])
    
for n in test_case[1:]:
    print(sums[int(n)-1])