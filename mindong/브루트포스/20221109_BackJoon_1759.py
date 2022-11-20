l, c = map(int, input().split())
chars=input().split()
chars.sort()
def permutation(string, chars, l, vowel, consonant):
    if string=="":
        vowel, consonant=0,0
    for i, char in enumerate(chars):
        if char in ["a","e","i","o","u"]:
            vowel+=1
        else:
            consonant+=1
        string+=char
        if l==1:
            if vowel>=1 and consonant>=2:
                print(string)
        else:
            chars=chars[1:]
            l-=1
            permutation(string, chars, l, vowel, consonant)
            l+=1
        string=string[:-1]
        if char in ["a","e","i","o","u"]:
            vowel-=1
        else:
            consonant-=1
permutation("", chars, l, 0, 0)