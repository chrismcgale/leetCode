class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def findScore(left, right) -> int:
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            
            score = max(nums[left] - findScore(left + 1, right), nums[right] - findScore(left, right - 1))
            memo[(left, right)] = score
            return memo[(left, right)]
    
        return findScore(0, len(nums) - 1) >= 0
    
    def predictTheWinnerTopDown(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        # dp[i][j] means nums i - j still available so max value for dp[i][i] is nums[i]
        for i in range(n):
            dp[i][i] = nums[i]
            
        # Work your way up and right solving for the best they can achieve
        for d in range(1, n):
            for left in range(n - d):
                right = left + d
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])
                
        return dp[0][n - 1] >= 0
    
    def predictTheWinnerBetterSpace(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        
        # Work your way up and right solving for the best they can achieve
        for d in range(1, n):
            for left in range(n - d):
                right = left + d
                # Update dp in place for space optimization
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
                
        return dp[0] >= 0