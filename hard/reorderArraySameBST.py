class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(lst: List[int]) -> int:
            m = len(lst)
            if m < 3:
                return 1
            left = [a for a in lst if a < lst[0]]
            right = [a for a in lst if a > lst[0]]
            return dfs(left) * dfs(right) * comb(m - 1, len(left)) % mod
            
        return (dfs(nums) - 1) % mod