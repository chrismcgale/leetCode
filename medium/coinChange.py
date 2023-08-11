class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
            
        return dp[amount]
        
        
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def numberOfWays(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == len(coins):
                return 0

            if coins[i] > amount:
                return numberOfWays(i + 1, amount)
            else:
                return numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)

        return numberOfWays(0, amount)