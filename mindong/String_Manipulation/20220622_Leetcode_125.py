# 125. Valid Panlindrome
# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphanumeric_s=re.sub("[^a-zA-Z0-9]", "", s).lower() #알파벳과 숫자만 남기고 소문자로 변경
        len_s=len(alphanumeric_s)
        
        for i in range(len_s//2): 
            if alphanumeric_s[i]!=alphanumeric_s[len_s-i-1]: #문자열을 반으로 나눠 대칭되는 인덱스의 값끼리 비교
                return False
        
        return True

