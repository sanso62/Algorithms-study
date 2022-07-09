class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        left, right=0, len(prices)-1
        while left+1<right and prices[left] >= prices[left+1]:
            left+=1   
        while left<right-1 and prices[right] <= prices[right-1]:
            right-=1
        while left<right:
            for i in range(left+1,right+1):
                if prices[i]-prices[left]>profit:
                    profit=prices[i]-prices[left]
            while left<right:
                e=1   
                while left+e<=right and prices[left] <= prices[left+e]:
                    e+=1
                left+=e
                for i in range(left+1,right+1):
                    if prices[i]-prices[left]>profit:
                        profit=prices[i]-prices[left]
            f=1
            while right-f>left and prices[right] >= prices[right-f]:
                f+=1

        return profit

"""
    121. Best Time to Buy and Sell Stock
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    1. 왼쪽 오른쪽을 각각 이동시키면서, 제외시킬만한것들 소거해가기
    2. 
    3. O(N)
    4. 
    5. O(N)를 만들기 위해 여러 소거법을 적용했다. 
       모두 구현하고 나서 다시보니 간단한 알고리즘이었지만,
       힘들었던 문제였다.
"""