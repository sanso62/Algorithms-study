# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        start=[]
        end=[]
        for interval in intervals:
            if (not start) and (not end):
                start.append(interval[0])
                end.append(interval[1])
            elif interval[0]<=end[-1]:
                if interval[1]> end[-1]:
                    end.pop()
                    end.append(interval[1])
            else:
                start.append(interval[0])
                end.append(interval[1])
            
        result = []
        for i in range(len(start)):
            result.append([start[i],end[i]])
        
        return result