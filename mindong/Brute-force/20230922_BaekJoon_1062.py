N, K = map(int, input().split())

words=[]
for _ in range(N):
    words.append(input())

alphabet = {"b": False, "d":False, "e":False,
            "f":False, "g":False, "h":False, "j":False,
            "k":False, "l":False, "m":False, "o":False,
            "p":False, "q":False, "r":False, "s":False,
            "u":False, "v":False, "w":False, "x":False, 
            "y":False, "z":False}
keys = list(alphabet.keys())

def can_read1(word, alph):
    for c in word:
        if not alph[c]:
            return False
    return True

def can_read2(word, alph):
    for c in word:
        if alph[c]:
            return False
    return True
    

def combination1(n, start, alph):
    global ans
    # print("combination1")
    if n == 0:
        result = 0
        for c in ["a", "c", "i", "n", "t"]:
            alph[c] = True
        for word in words:
            if can_read1(word[4:-4], alph):
                result+=1
        if result>ans:
            ans = result
        return
    for i in range(start, len(keys)):
        # print(n, i, start)
        alph[keys[i]] = True
        combination1(n-1, i+1, alph)
        alph[keys[i]] = False

def combination2(n, start, alph):
    global ans
    # print("combination2")
    if n == 0:
        result = 0
        for c in ["a", "c", "i", "n", "t"]:
            alph[c] = False
        for word in words:
            if can_read2(word[4:-4], alph):
                result+=1
        if result>ans:
            ans = result
        return
    for i in range(start, len(keys)):
        # print(n, i, start)
        alph[keys[i]] = True
        combination2(n-1, i+1, alph)
        alph[keys[i]] = False

ans = 0
if K-5 < 0:
    ans = 0
elif K-5 < 12:
    combination1(K-5, 0,alphabet)
elif K-5 < 22:
    combination2(21-(K-5), 0, alphabet)

print(ans)