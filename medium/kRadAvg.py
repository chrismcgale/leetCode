class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        out = [-1 for _ in range(n)]
        step = nums[:]
        
        if k == 0:
            return nums
        
        if n < 2 * k + 1:
            return out
        
        for i in range(1, n):
            step[i] += step[i - 1] 
            
              
        out[k] = step[2 * k] // (2 * k + 1)
        
        for i in range(2 * k + 1, n):
            num = step[i] - step[i - (2 * k + 1)]
            out[i - k] = num // (2 * k + 1)
            
        return out