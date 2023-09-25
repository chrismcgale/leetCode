class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * i for i in range(1, 101)]
        
        tower[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(i + 1):
                spill = (tower[i][j] - 1.0) / 2.0
                if spill > 0:
                    tower[i+1][j] += spill
                    tower[i+1][j+1] += spill
            
        return min(tower[query_row][query_glass], 1.0)