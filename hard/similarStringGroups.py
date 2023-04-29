class Solution:
    def similar(self, i: str, j: str) -> bool:
        if i == j:
            return True
        
        diff = 0
        for k in range(0, len(i)):
            if (i[k] != j[k]):
                diff += 1
        
        return diff == 2
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = [[] for j in range(n)] 
        visited = [False for j in range(n)] 
        count = 0
        
        print(adj)

        
        for i in range(0, n):
            for j in range(i + 1, n):
                if self.similar(strs[i], strs[j]):
                    print(i, j)
                    adj[i].append(j)
                    adj[j].append(i)
                    
        def dfs(i):
            nonlocal adj
            nonlocal visited
            q = []
            q.append(i)
            visited[i] = True
            
            while len(q) > 0:
                n = q.pop(0)
                
                for p in adj[n]:
                    if not visited[p]:
                        visited[p] = True
                        q.append(p)
                    
                    
        for i in range(0, n):
            if not visited[i]:
                dfs(i)
                count += 1
                
        return count