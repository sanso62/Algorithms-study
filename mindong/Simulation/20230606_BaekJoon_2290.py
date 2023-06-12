s, n = input().split()
s=int(s)
n = list(n)

part1 = [" "+"-"*(s)+" " for _ in range(len(n))]
part2 = ["" for _ in range(len(n))]
part3 = [" "+"-"*(s)+" " for _ in range(len(n))]
part4 = ["" for _ in range(len(n))]
part5 = [" "+"-"*(s)+" " for _ in range(len(n))]

for i, num in enumerate(n):
    if num=="1":
        part1[i]=" "*(s+2)
        part2[i]=" "*(s+1)+"|"
        part3[i]=" "*(s+2)
        part4[i]=" "*(s+1)+"|"
        part5[i]=" "*(s+2)
    elif num=="2":
        part2[i]=" "*(s+1)+"|"
        part4[i]="|"+" "*(s+1)
    elif num=="3":
        part2[i]=" "*(s+1)+"|"
        part4[i]=" "*(s+1)+"|"
    elif num=="4":
        part1[i]=" "*(s+2)
        part2[i]="|"+" "*(s)+"|"
        part4[i]=" "*(s+1)+"|"
        part5[i]=" "*(s+2)
    elif num=="5":
        part2[i]="|"+" "*(s+1)
        part4[i]=" "*(s+1)+"|"
    elif num=="6":
        part2[i]="|"+" "*(s+1)
        part4[i]="|"+" "*(s)+"|"
    elif num=="7":
        part2[i]=" "*(s+1)+"|"
        part3[i]=" "*(s+2)
        part4[i]=" "*(s+1)+"|"
        part5[i]=" "*(s+2)
    elif num=="8":
        part2[i]="|"+" "*(s)+"|"
        part4[i]="|"+" "*(s)+"|"
    elif num=="9":
        part2[i]="|"+" "*(s)+"|"
        part4[i]=" "*(s+1)+"|"
    elif num=="0":
        part2[i]="|"+" "*(s)+"|"
        part3[i]=" "*(s+2)
        part4[i]="|"+" "*(s)+"|"

print(" ".join(part1))
for _ in range(s):
    print(" ".join(part2))
print(" ".join(part3))
for _ in range(s):
    print(" ".join(part4))
print(" ".join(part5))