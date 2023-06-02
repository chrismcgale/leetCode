class Solution:
    # Each bomb is x, y, radius
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Construct directed graph
        n = len(bombs)
        adj = [[] for _ in range(n)]
        
        def reaches(x1, y1, r, x2, y2):
            return r >= math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j and reaches(x1, y1, r1, x2, y2):
                    adj[i].append(j)
                    
        
        def dfs(start: int) -> int:
            stack = [start]
            visited = [False for _ in range(n)]
            visited[start] = True
            popped = 0
            
            while stack:
                curr = stack.pop()
                popped += 1
                
                for neigh in adj[curr]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        stack.append(neigh)
                        
            return popped
                    
        
        # Run dfs from every bomb
        return max(dfs(i) for i in range(n))