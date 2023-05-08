class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)
        for i in range(n):
            res += mat[i][i] 
            res += mat[i][n - i - 1]
            
        if n % 2 == 1:
            mid = n // 2
            res -= mat[mid][mid]
            
        return res