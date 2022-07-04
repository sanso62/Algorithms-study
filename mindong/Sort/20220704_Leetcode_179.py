class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=[[],[],[],[],[],[],[],[],[],[]]
        nums=list(map(str, nums))
        for i in nums:
            n[int(str(i)[0])].append(i)
        
        def merge_sort(li):
            if len(li)<2:
                return li
            left=li[:len(li)//2]
            right=li[len(li)//2:]
            left=merge_sort(left)
            right=merge_sort(right)
            return merge(left, right)
        
        def merge(left, right):
            result=[]
            while left or right:
                if left and right:
                    if int(left[0]+right[0]) >= int(right[0]+left[0]):
                        result.append(left.pop(0))
                    else:
                        result.append(right.pop(0))
                
            
                elif left:
                    result.append(left.pop(0))
                elif right:
                    result.append(right.pop(0))
                    
            return result
                
        answer=""
        for l in n:
            l=merge_sort(l)
            answer= "".join(l)+answer
            
        if len(answer)>1 and answer[0]=="0":
            return "0"
        
        return answer