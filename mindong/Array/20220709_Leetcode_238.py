class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        p=1
        for i in range(len(nums)):
            result.append(p)
            p*=nums[i]
        
        p=1
        for j in range(len(nums)-1, -1, -1):
            result[j]*=p
            p*=nums[j]
        
        return result

"""
    238. Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/
    
    1. 순서대로 누적시키면서 곱하고, 다시 역순으로 누적시키면서 곱
    2. 
    3. O(N)
    4.
    5. 거의 근접했는데, 결국 못풀었다..
"""