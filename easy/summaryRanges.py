class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        last = nums[0]
        curr = str(nums[0])
        
        for i in nums[1:]:
            if last != i - 1:
                if curr != str(last):
                    curr += "->" + str(last)
                ans.append(curr)
                curr = str(i)
            
            last = i
            
        if curr != str(last):
            curr += "->" + str(last)
                
        ans.append(curr)
                
        return ans