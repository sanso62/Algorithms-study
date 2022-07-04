class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[j]==0:
                j+=1
            else:
                nums.append(nums.pop(j))
        
        k=j
        for i in range(len(nums[j:])):
            if nums[k]==1:
                k+=1
            else:
                nums.append(nums.pop(k))