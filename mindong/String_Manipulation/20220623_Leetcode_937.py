# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/
import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs=[]
        digit_logs=[]
        
        for i, log in enumerate(logs):
            not_digit=bool(re.sub("\d", "", log[-1]))
            if not_digit:
                letter_logs.append(logs[i])
            else:
                digit_logs.append(logs[i])
        
        # print(letter_logs)
        space_i=[]
        for letter_log in letter_logs:
            for j,c in enumerate(letter_log):
                if c==" ":
                    space_i.append(j)
                    break
                    
        split_letter_logs=[]
        for k, idx in enumerate(space_i):
            split_letter_logs.append((letter_logs[k][:idx], letter_logs[k][idx+1:]))
        
        split_letter_logs.sort(key=lambda split_letter_log: split_letter_log[0])
        split_letter_logs.sort(key=lambda split_letter_log: split_letter_log[1])
        
        letter_logs.clear()
        for split_log in split_letter_logs:
            letter_logs.append(split_log[0]+" "+split_log[1])
        
        return letter_logs+digit_logs
        
        
            
            
                
                
            