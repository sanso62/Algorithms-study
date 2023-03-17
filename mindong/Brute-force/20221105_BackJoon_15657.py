n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
visited=nums[:]
def permutation(li, nums, visited, m, i):
    for num in visited:
        li.append(str(num))
        if m==1:
            print(" ".join(li))
        else:
            # print("***",i, id(i), num, nums)
            visited=nums[i:]
            m-=1
            permutation(li, nums, visited, m, i)
            i+=1
            m+=1
        li.pop()
permutation([], nums, visited, m, 0)