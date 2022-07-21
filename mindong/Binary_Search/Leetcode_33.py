import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=0
        if nums[0]>=nums[-1]:
            start=0
            end=len(nums)-1
            while start<=end:
                pointer=(end-start+1)//2+start
                if pointer-1<0:
                    break
                else:
                    if nums[pointer]>nums[-1]:
                        start=pointer+1
                    elif nums[pointer]<=nums[-1] and nums[pointer-1]>nums[-1]:
                        pivot=pointer-1
                        break
                    else:
                        end=pointer-1
        
        index=bisect.bisect_left(nums, target, lo=0 , hi=pivot+1)
        if index<len(nums) and nums[index]==target:
            return index

        index=bisect.bisect_left(nums, target, lo=pivot+1, hi=len(nums))
        if index<len(nums) and nums[index]==target:
            return index
        return -1