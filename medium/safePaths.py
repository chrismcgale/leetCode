class Solution:
    def eventualSafeNodesRecur(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        visited = [False] * n
        inStack = [False] * n
        
        def dfs(node, adj, visited, inStack) -> bool:
             # If the node is already in the stack, we have a cycle.
            if inStack[node]:
                return True
            if visited[node]:
                return False
            # Mark the current node as visited and part of current recursion stack.
            visited[node] = True
            inStack[node] = True
            for n in adj:
                if dfs(n, graph[n], visited, inStack):
                    return True
            # Remove the node from the stack.
            inStack[node] = False
            return False
        
        for i, adj in enumerate(graph):
            dfs(i, adj, visited, inStack)
                
                
        for i in range(n):
            if not inStack[i]:
                res.append(i)
                
        return res