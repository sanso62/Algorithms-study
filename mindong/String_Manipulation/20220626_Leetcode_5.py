class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in list(range(len(s)+1))[::-1]:
            if i == 1 or i==0:
                return s[0]
            
            for j in range(len(s)-i+1):
                sub_s=s[j:j+i]
                if sub_s==sub_s[::-1]:
                    return sub_s