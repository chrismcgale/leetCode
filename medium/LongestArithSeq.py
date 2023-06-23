class Solution:    
    def findPattern(self, nums: List[int], start) -> int:
        if not nums:
            return 0
        
        def continuePattern(nums: List[int], start, step) -> int:
            ans = 0
            for i in nums:
                if i == start + step:
                    ans += 1
                    start += step

            return ans

        return max(continuePattern(nums[i:], start, n - start) for i, n in enumerate(nums))
    
    # Could work in time limit but requires hashing a list
    def longestArithSeqLengthBruteForce(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        # Option 1: first index is start of sequence and some number after continues it
        start = 1 + self.findPattern(nums[1:], nums[0])
        
        # Option 2: start of seq is some other index
        some = self.longestArithSeqLength(nums[1:])
        
        return max(start, some)
    
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1   
        
        return max(dp.values())