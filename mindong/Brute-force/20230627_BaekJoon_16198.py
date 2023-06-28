N = int(input())
W = list(map(int, input().split()))

max_value=0
def choose_energy(value, n, check):
    global max_value
    if n==2:
        if max_value<value:
            max_value=value
        return
    for i in range(1, N-1):
        if not check[i]:
            add=0
            for j in range(i-1, -1, -1):
                if not check[j]:
                    left=j
                    break
            for k in range(i+1, N):
                if not check[k]:
                    right=k
                    break
            check[i]=TrueSS
            choose_energy(value+W[left]*W[right], n-1, check)
            check[i]=False

choose_energy(0, N, [False for _ in range(N)])
print(max_value)