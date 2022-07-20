class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer=len(nums)//2
        start=0
        end=len(nums)-1
        while start<=end:
            if nums[pointer]==target:
                return pointer
            elif nums[pointer]<target:
                start=pointer+1
                pointer=(end-start+1)//2+start
            else:
                end=pointer-1
                pointer=(end-start+1)//2+start
        
        return -1
        
        