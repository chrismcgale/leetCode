class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        ans = 0
        
        def dfs(start):
            nonlocal ans
            ans += 1
            
            visited[start] = True
            stack = [start]
            
            while stack:
                curr = stack.pop()
                
                for i, connected in enumerate(isConnected[curr]):
                    if connected and not visited[i]:
                        visited[i] = True
                        stack.append(i)
            
        for i in range(n):
            if not visited[i]:
                dfs(i)
            
        return ans
            