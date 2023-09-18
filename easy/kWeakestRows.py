class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        
        n, m = len(mat), len(mat[0])
        
        for c in range(m):
            for r in range(n):
                if len(res) == k:
                    break
                    
                if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
                    res.append(r)
                    
        i = 0
        while len(res) < k:
            if mat[i][-1] == 1:
                res.append(i)
            i += 1
                    
        return res