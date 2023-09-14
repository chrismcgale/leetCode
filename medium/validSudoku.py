class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                
                # Check if position is filled
                if val == ".":
                    continue
                    
                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # Check col
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                
                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
                  
        return True