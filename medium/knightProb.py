class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]

        def calcProp(moves, i, j) -> float:  
            if dp[moves][i][j] != -1:
                return dp[moves][i][j]

            dp[moves][i][j] = 0

            if moves == 0:
                dp[moves][i][j] = 1
                return 1
            
            for d in dirs:
                if 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                    dp[moves][i][j] += calcProp(moves - 1, i + d[0], j + d[1])
                    
            dp[moves][i][j] /= 8

            return dp[moves][i][j]
        
        calcProp(k, row, column)
        
        return dp[k][row][column]