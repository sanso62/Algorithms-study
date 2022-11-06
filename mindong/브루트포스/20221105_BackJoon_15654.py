n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
visited=nums[:]
def permutation(li, nums, visited, m):
    for i, num in enumerate(visited):
        if num!=-1:
            li.append(str(num))
            if m==1:
                print(" ".join(li))
            else:
                visited[i]=-1
                m-=1
                permutation(li, nums, visited, m)
                visited[i]=nums[i]
                m+=1
            li.pop()
permutation([], nums, visited, m)