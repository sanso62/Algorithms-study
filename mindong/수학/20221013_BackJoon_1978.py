import sys

input=sys.stdin.read().splitlines()
n_list=list(map(int, input[1].split()))
num=0
for n in n_list:
    if n<=1:
        continue
    elif 1<n<4:
        num+=1
    else:
        num+=1
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                num-=1
                break
            
print(num)