class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results

"""
    15. 세수의 합
    https://leetcode.com/problems/3sum/
    
    1. 정렬하고 브루트포스로 접근한다음 최대한 생략할 건 생략한다.
       -> 하나는 순서대로 루프하고 나머지 두개의 인덱스를 세수의 합이 0을 기준으로 각자 이동한다.
    2. 브루트포스
    3. O(N^2)
    4.
    5. 느낀점: 이것은 책 풀이다. 
               나의 원래 풀이도 브루트포스로 접근한다음
               세수의 합을 기준으로 인덱스를 이동시켰지만,
               기준이 되는 인덱스를 두개로 설정해,
               0이 될때, 어떤 인덱스를 이동시켜야 할지 고민하다가 못풀었다.
               거의 3시간 동안 풀었고,
               완전 스파게티 코드였다.
"""