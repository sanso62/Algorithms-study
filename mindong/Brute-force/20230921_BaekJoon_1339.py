N = int(input())
words = []
for _ in range(N):
    words.append(input())

weights = {}
for word in words:
    for i, c in enumerate(word[::-1]):
        if c not in weights:
            weights[c] = 10**i
        else:
            weights[c] += 10**i

alphabets = sorted(weights, key= lambda x: weights[x], reverse=True)
num, total = 9, 0
for c in alphabets:
    total += weights[c]*num
    num-=1

print(total)

"""
10**7() + 10**6() + ... + 10**0()
1. 꼭 A~J까지만 있는 건 아님.
2. 높은 자리에 있는 알파벳부터 높은 숫자 부여하는게 좋음
3.  자릿수를 가중치로 더해서 높은 알파벳부터 높은 숫자를 부여

1. 주어진 단어 순서대로 알파벳이 새로 등장하면 딕셔너리에 추가하고 있으면 값 더하기
2. 자릿수는 오른쪽 인덱스부터 부여
"""