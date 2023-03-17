import sys

inputs=sys.stdin.read().splitlines()
heights=list(map(int, inputs))
heights.sort()
sum_heights=sum(heights)
li=[sum_heights-heights-100 for heights in heights]

find=False
for i in range(len(heights)):
    for j in range(len(li)):
        if heights[i]==li[j]:
            heights[i]=-1
            heights[j]=-1
            find=True
            break
    if find:
        break

for h in heights:
    if h!=-1:
        print(h)
        
# O(N)=N^2