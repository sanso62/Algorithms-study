import sys

input=sys.stdin.read().splitlines()
n_list=list(map(int, input[1:]))

for n in n_list:
    g_n=1
    nums=[num for num in range(1,n+1)]
    nums[0]=0
    zeros=1
    while zeros<len(nums):
        for i in range(-1, -len(nums)-1, -1):
            if nums[i]!=0:
                big_num, nums[i]=nums[i], 0
                zeros+=1
                break
    
        big_num_divisors=[]
        for i in range(1,int(big_num**0.5)+1):
            if big_num%i==0:
                big_num_divisors.append(i)
                if i!=big_num//i:
                    big_num_divisors.append(big_num//i)
                
        big_num_divisors.sort()
        g_n+=sum(big_num_divisors)
        for j,m in enumerate(big_num_divisors[1:-1]):
            if nums[m-1]==0:
                continue
            else:
                nums[m-1]=0
                zeros+=1
            for k in big_num_divisors[:j+1]:
                if k>int(m**0.5):
                    break
                else:
                    if m%k==0:
                        if k==m//k:
                            g_n+=k
                        else:
                            g_n+=k+m//k
    print(g_n)