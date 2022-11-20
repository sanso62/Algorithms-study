n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
def permutation(li, nums, m):
    for i, num in enumerate(nums):
        li.append(str(num))
        if m==1:
            print(" ".join(li))
        else:
            # print("***",num, nums)
            m-=1
            permutation(li, nums, m)
            m+=1
        li.pop()
permutation([], nums, m)