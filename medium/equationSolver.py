class Solution:
    # Equations formatted as [A, B] where A_i / B_i = values[i]
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        res = []
        
        # Construct graph
        for i, e in enumerate(equations):
            if e[0] not in graph:
                graph[e[0]] = {e[1] : values[i]}
            else:
                graph[e[0]][e[1]] = values[i]
                
            if e[1] not in graph:
                graph[e[1]] = {e[0] : 1 / values[i]}
            else:
                graph[e[1]][e[0]] = 1 / values[i]
             
        def dfs(start, end):
            visited = {}
            if start not in graph or end not in graph:
                return -1
            
            if start == end:
                return 1
            
            stack = [(start, 1)]
            
            while stack:
                node, curr = stack.pop()
                visited[node] = True
                for connect in graph[node]:
                    push = curr * graph[node][connect]
                    if connect == end:
                        return push
                    elif connect not in visited:
                        stack.append((connect, push))
            return -1

        # Run dfs on each equation
        for q in queries:
            res.append(dfs(q[0], q[1]))
            
        return res