class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        m = s = 0
        sums = {}
        
        for i in range(len(nums)):
            s += nums[i]
            
            if s == k:
                m = i + 1
                
            if s not in sums:
                sums[s] = i
            
            if s - k in sums:
                m = max(m, i - sums[s - k])
                
                
        return m