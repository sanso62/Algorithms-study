n, m = map(int, input().split())
nums=[i for i in range(1,n+1)]
def permutation(li, nums, m):
    for i, num in enumerate(nums):
        li+=" "+str(num)
        if m==1:
            print(li[1:])
        else:
            # print("***",num, nums)
            nums=nums[1:]
            m-=1
            permutation(li, nums, m)
            m+=1
        li=li[:-2]
permutation("", nums, m)