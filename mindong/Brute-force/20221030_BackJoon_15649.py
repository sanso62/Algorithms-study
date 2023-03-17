n, m = map(int, input().split())
nums=[i for i in range(1,n+1)]
visited=nums[:]
def permutation(li, nums, visited, m):
    for i, num in enumerate(visited):
        if num!=-1:
            li+=" "+str(num)
            if m==1:
                print(li[1:])
            else:
                visited[i]=-1
                m-=1
                permutation(li, nums, visited, m)
                visited[i]=nums[i]
                m+=1
            li=li[:-2]
permutation("", nums, visited, m)