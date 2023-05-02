class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firsts = []
        
        for (r, l) in enumerate(board):
            for (c, s) in enumerate(l):
                if s == word[0]:
                    firsts.append([r, c, 0])
                    
        if len(word) == 1 and len(firsts) > 0:
            return True
                    
        def dfs(node):
            nonlocal visited
            r, c, i = node[0], node[1], node[2]
            visited[r][c] = True

            once = False
            
            directions = [[r - 1, c] if r > 0 else [], [r + 1, c] if r + 1 < len(board) else [], [r, c - 1] if c > 0 else [], [r, c + 1] if c + 1 < len(board[0]) else []]
            
            for coord in directions:
                if coord and board[coord[0]][coord[1]] == word[i + 1] and not visited[coord[0]][coord[1]]:
                    if i + 2 == len(word):
                        return True

                    if dfs([coord[0], coord[1], i + 1]):
                        return True

            visited[r][c] = False        
                    
        for coord in firsts:
            visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
            if dfs(coord):
                return True
        return False