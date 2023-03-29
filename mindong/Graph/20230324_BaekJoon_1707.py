# #bfs
# import collections

# k=int(input())
# result=["YES" for _ in range(k)] 
# for i in range(k):
#     V, E=map(int, input().split())
#     A=[[] for _ in range(V)]
#     li_v=[]
#     for _ in range(E):
#         u,v=map(int, input().split())
#         if len(A[u-1])==0:
#             li_v.append(u)
#         if len(A[v-1])==0:
#             li_v.append(v)
#         A[u-1].append(v)
#         A[v-1].append(u)
    

#     checked=[[False,0] for _ in range(V)]
#     for start in li_v:
#         if checked[start-1][0]:
#             continue
#         side=1
#         checked[start-1]=[True, side]
#         q=collections.deque()
#         q.append(start)
#         while len(q)>0:
#             # print(len(q),checked)
#             if result[i]=="NO":
#                 break
#             cur=q.popleft()
#             if checked[cur-1][1]==1: side=2
#             elif checked[cur-1][1]==2: side=1
#             for vertex in A[cur-1]:
#                 if checked[vertex-1][0]:
#                     if checked[vertex-1][1]==checked[cur-1][1]:
#                         result[i]="NO"
#                         break
#                 else:
#                     checked[vertex-1]=[True, side]
#                     q.append(vertex)

# for r in result:
#     print(r)
        

# dfs
import sys
sys.setrecursionlimit(20003)
k=int(input())
result=["YES" for _ in range(k)] 
for i in range(k):
    V, E=map(int, input().split())
    A=[[] for _ in range(V)]
    li_v=[]
    for _ in range(E):
        u,v=map(int, input().split())
        if len(A[u-1])==0:
            li_v.append(u)
        if len(A[v-1])==0:
            li_v.append(v)
        A[u-1].append(v)
        A[v-1].append(u)

    
    checked=[[False,0] for _ in range(V)]
    def dfs(x, side):
        global checked
        if result[i]=="NO":
            return
        for vertex in A[x-1]:
            if checked[vertex-1][0]:
                if checked[vertex-1][1]==checked[x-1][1]:
                    result[i]="NO"
                    return 
            else:
                checked[vertex-1][0]=True
                if side==1:
                    checked[vertex-1][1]=2
                    # print(checked)
                    dfs(vertex,2)
                elif side==2:
                    checked[vertex-1][1]=1
                    # print(checked)
                    dfs(vertex,1)

    for start in li_v:
        if checked[start-1][0]==False:
            checked[start-1]=[True, 1]
            check_count=1
            # print(checked)
            dfs(start, 1)

for r in result:
    print(r)
