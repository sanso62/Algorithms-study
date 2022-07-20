import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        for li in matrix:
            index=bisect.bisect_left(li, target)
            if index<n and li[index]==target:
                return True
        
        return False