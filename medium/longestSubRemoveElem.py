class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last, m, zeros = -1, 0, 0
        
        for i, n in enumerate(nums):
            if n == 0:
                zeros = last + 1
                last = i
                
            m = max(m, i - zeros)
                
        return m