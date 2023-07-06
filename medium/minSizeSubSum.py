class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        currSum = 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            
            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1

        return res if res != float('inf') else 0