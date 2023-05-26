class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @cache
        def Alice(index: int, X: int) -> int:
            if index >= n:
                return 0
    
            return max(sum(piles[index : index + i]) + Bob(index + i, max(X, i)) for i in range(1, 2 * X + 1))

        
        @cache
        def Bob(index: int, X: int) -> int:
            if index >= n:
                return 0
            
            return min(Alice(index + i, max(X, i)) for i in range(1, 2 * X + 1))
        
        
        return Alice(0, 1)
    
    def fasterStoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1] 
        
        @cache
        def dp(index: int, X: int) -> int:
            if index + 2 * X >= n:
                return piles[index]
    
            return piles[index] - min(dp(index + i, max(X, i)) for i in range(1, 2 * X + 1))

        
        return dp(0, 1)