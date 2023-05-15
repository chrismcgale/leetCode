class Solution:
    # Counts number of ways to tile all strings of length low - high using continuous tiles of length one and zero
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        mod = 10 ** 9 + 7
        
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod
            
        return sum(dp[low:high + 1]) % mod