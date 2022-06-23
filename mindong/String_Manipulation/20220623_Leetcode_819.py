# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = re.sub("[^a-zA-Z0-9]"," ", paragraph).lower()
        words=s.split()
        
        n_word={}
        for w in words:
            if w in n_word:
                n_word[w]+=1
            else:
                n_word[w]=1
        
        sorted_n_word=sorted(n_word, key=lambda x: n_word[x], reverse=True)
        
        for word in sorted_n_word:
            if word not in banned:
                return word