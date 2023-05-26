class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @cache
        def Alice(index: int, X: int) -> int:
            if index >= n:
                return 0
            
            m = 0
            for i in range(1, 2 * X + 1):
                m = max(m, sum(piles[index : index + i]) + Bob(index + i, max(X, i)))
        
            return m
        
        @cache
        def Bob(index: int, X: int) -> int:
            if index >= n:
                return 0
            
            m = sys.maxsize
            for i in range(1, 2 * X + 1):
                m = min(m, Alice(index + i, max(X, i)))
        
            return m
        
        return Alice(0, 1)