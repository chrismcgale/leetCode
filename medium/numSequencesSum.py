class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res, mod = 0, 10 ** 9 + 7
        left, right = 0, len(nums) - 1
        nums.sort()
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1

        return res