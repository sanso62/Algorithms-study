# 15649번 N과 M(1)

def nm_func(add_num):
    global m, arr_num, visited

    if(len(add_num) == m):
        arr = list(add_num)
        for num in arr:
            print(num, end=' ')

        print()
        return

    for cur_num in arr_num:
        if(visited[cur_num-1] == 0):
            visited[cur_num-1] = 1
            nm_func(add_num+str(cur_num))
            visited[cur_num - 1] = 0


n, m = map(int, input().split())

arr_num = []
visited = []
for i in range(1, n+1):
    arr_num.append(i)
    visited.append(0)

nm_func('')