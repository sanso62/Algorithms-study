import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        if len(nums1)>len(nums2):
            nums1.sort()
            nums2=list(set(nums2))
            for target in nums2:
                index=bisect.bisect_left(nums1, target)
                if index<len(nums1) and nums1[index]==target:
                    result.append(target)
        else:
            nums2.sort()
            nums1=list(set(nums1))
            for target in nums1:
                index=bisect.bisect_left(nums2, target)
                if index<len(nums2) and nums2[index]==target:
                    result.append(target)
        
        return result
                
        