class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(0, len(nums),2):
            result+=nums[i]
        return result

"""
    561. 배열 파티션 I
    https://leetcode.com/problems/array-partition/
    
    1. 예시를 살펴보니 규칙이 보인다. 
       최대한 크기가 비슷한 것끼리 합친다음
       최솟값을 구해야 최대값이 나온다.
       정렬->짝수번 인덱스만 합
    2. 정렬
    3. O(NlogN)
    4. 
    5. 규칙찾는 것도 중요한 역량일듯..

    
"""