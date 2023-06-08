class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        currRowNeg = n - 1
        ans = 0
        
        for row in grid:
            while currRowNeg >= 0 and row[currRowNeg] < 0:
                currRowNeg -= 1
            ans += (n - currRowNeg - 1)
        
        return ans