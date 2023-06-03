class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for _ in range(n)]
        maxTime = 0
        
        # Construct tree
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)
                
        queue = [(headID, 0)]
        
        while queue:
            parent, time = queue.pop(0)
            
            maxTime = max(maxTime, time)
            
            for emp in adj[parent]:
                queue.append((emp, time + informTime[parent]))
                
        return maxTime