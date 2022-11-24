n=int(input())
permutation=list(map(int,input().split()))

max=-1
def choose(li, length, prev, sum):
    global max
    if length==0:
        if sum>max:
            max=sum
        return
    for i in range(length):
        li[i],li[-1]=li[-1],li[i]
        temp=li.pop()
        if length<n:
            choose(li, length-1, temp, sum+abs(prev-temp))
        else:
            choose(li, length-1, temp, 0)
        li.append(temp)
        li[i],li[-1]=li[-1],li[i]

choose(permutation, n, 0, 0)

print(max)