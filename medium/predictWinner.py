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
    