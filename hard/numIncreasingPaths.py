class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        visited = {}   
        res = 0
          
        @cache
        def dfs(i, j):
            paths = 1
            
            if 0 <= i - 1 and grid[i][j] < grid[i - 1][j]:
                paths += dfs(i - 1, j) % mod

            if i + 1 < m and grid[i][j] < grid[i + 1][j]:
                paths += dfs(i + 1, j) % mod

            if 0 <= j - 1 and grid[i][j] < grid[i][j - 1]:
                paths += dfs(i, j - 1) % mod

            if j + 1 < n and grid[i][j] < grid[i][j + 1]:
                paths += dfs(i, j + 1) % mod
                    
            return paths

        # Run dfs on each equation
        for i in range(m):
            for j in range(n):
                res += dfs(i, j) % mod
            
        return res % mod