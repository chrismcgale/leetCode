class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break
            
        first_queue = [(first_x, first_y)]
        second_queue = [(first_x, first_y)]
        grid[first_x][first_y] = 2

        while first_queue:
            new_bfs = []
            for x, y in first_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                        new_bfs.append((cur_x, cur_y))
                        second_queue.append((cur_x, cur_y))
                        grid[cur_x][cur_y] = 2
            first_queue = new_bfs
 
    
        distance = 0
        while second_queue:
            new_bfs = []
            for x, y in second_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1
            second_queue = new_bfs
            distance += 1