#graph
n, m= map(int, input().split())
cor=[[0]*n for _ in range(n)]
v_li=[[] for _ in range(n)]
e_li=[]

for _ in range(m):
    a, b=map(int, input().split())
    cor[a][b], cor[b][a]=1, 1
    v_li[a].append(b)
    v_li[b].append(a)
    e_li.append([a,b])
    e_li.append([b,a])

e_li.sort()
# print(cor)
# print(v_li)
# print(e_li)

found=False
for i in range(m*2):
    for j in range(m*2):
        A,B=e_li[i]
        C,D=e_li[j]
        # print(A,B,C,D)
        if A==B or A==C or A==D or B==C or B==D or C==D:
            continue
        if not cor[B][C]:
            continue
        for v in v_li[D]:
            # print(A,B,C,D,v)
            if v not in [A,B,C,D]:
                print(1)
                found=True
                break
        if found:
            break
    if found:
        break

if not found:
    print(0)

#Back_tracking
# n,m = map(int, input().split())
# graph=[[] for _ in range(n)]
# ans=0
# for _ in range(m):
#     a,b =map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def next(num, li):
#     global ans
#     if num==5:
#         ans=1
#         return 1
#     else:
#         for k in graph[li[-1]]:
#             if k not in li:
#                 next(num+1, li+[k])

# for i in range(n):
#     li=[i]
#     for j in graph[i]:
#         next(2, li+[j])
#         if ans==1:
#             break
#     if ans==1:
#         break

# print(ans)
