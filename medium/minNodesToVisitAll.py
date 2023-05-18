class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = [False for _ in range(n)]
        req = []
        
        for edge in edges:
            visited[edge[1]] = True
        
        for i in range(n):
            if not visited[i]:
                req.append(i)
                
        return req