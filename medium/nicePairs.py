class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            
            return result
        
        diff = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        
        for i in nums:
            r = i - rev(i)
            
            diff[r] = diff.get(r, 0) + 1
            
        for k, v in diff.items():
            ans = (ans + comb(v, 2)) % MOD
            
        return ans