import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            index=bisect.bisect_left(numbers[i+1:], target-numbers[i])
            if (i+1+index)<len(numbers) and numbers[i+1+index]==target-numbers[i]:
                return [i+1, i+index+2]
        