# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tuples=[]
        for s in strs:
            tuples.append(tuple(sorted(s)))
        
        dic=collections.defaultdict(list)
        for i in range(len(strs)):
            dic[tuples[i]].append(strs[i])
        
        result=[]
        for key in dic:
            result.append(dic[key])
        
        return result
            