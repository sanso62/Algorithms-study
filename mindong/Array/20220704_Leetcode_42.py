class Solution:
    def trap(self, height: List[int]) -> int:
        right=0
        max_h=0
        for i in range(len(height)):
            if max_h<height[i]:
                max_h, right=height[i], i
                
        left=0
        while height[left]<max_h:
            left+=1
        
        if left==right:
            total=height[left]
        else:
            total=height[left]*(right-left+1)
            
        high=0
        j=0
        while j<left:
            if high<height[j]:
                high=height[j]
            total+=high
            j+=1
        
        high=0
        k=len(height)-1
        while k>right:
            if high<height[k]:
                high=height[k]
            total+=high
            k-=1
        
        return total-sum(height)
    
"""
    42. 빗물트래핑
    https://leetcode.com/problems/trapping-rain-water/submissions/
    1. 빗물이 가득찬 상태를 구한다음 층의 개수의 합을 빼서 빗물이 있는 구간만 계산
    2. 선형탐색
    3. O(N)
    4. 
    5.
    
    
"""