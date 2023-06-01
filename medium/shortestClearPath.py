class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        queue = [(0, 0)]
        grid[0][0] = -1
        
        while queue:
            curr_x, curr_y = queue.pop(0)
            for dx, dy in dirs:
                nx, ny = curr_x + dx, curr_y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = grid[curr_x][curr_y] - 1
                        queue.append((nx, ny))
                    
        return -1 if grid[n - 1][n - 1] == 0 else -grid[n - 1][n - 1]