class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        res = [row[:] for row in mat]
        
        visited = set()
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                      
        while queue:
            curr_i, curr_j, count = queue.popleft()

            if curr_i + 1 < m and (curr_i + 1, curr_j) not in visited:
                visited.add((curr_i + 1, curr_j))
                queue.append((curr_i + 1, curr_j, count + 1)) 
                res[curr_i + 1][curr_j] = count + 1

            if curr_i - 1 >= 0 and (curr_i - 1, curr_j) not in visited:
                visited.add((curr_i - 1, curr_j))
                queue.append((curr_i - 1, curr_j, count + 1))
                res[curr_i - 1][curr_j] = count + 1

            if curr_j + 1 < n and (curr_i, curr_j + 1) not in visited:
                visited.add((curr_i, curr_j + 1))
                queue.append((curr_i, curr_j + 1, count + 1))
                res[curr_i][curr_j + 1] = count + 1

            if curr_j - 1 >= 0 and (curr_i, curr_j - 1) not in visited:
                visited.add((curr_i, curr_j - 1))
                queue.append((curr_i, curr_j - 1, count + 1))
                res[curr_i][curr_j - 1] = count + 1
                    
        return res
    
    def updateMatrixDP(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        # Check all paths going right and down
        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
                        
                    dp[row][col] = min_neighbor + 1

        # Check all paths going up and left    
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
                        
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)

        return dp