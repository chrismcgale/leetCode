class Solution:
    def canFinishDFS(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        
            
        for p in prereqs:
            graph[p[0]].append(p[1])
            
        visited = [False] * numCourses
        inStack = [False] * numCourses
        
        def detectCycleDfs(node, visited, inStack) -> bool:
             # If the node is already in the stack, we have a cycle.
            if inStack[node]:
                return True
            if visited[node]:
                return False
            # Mark the current node as visited and part of current recursion stack.
            visited[node] = True
            inStack[node] = True
            for n in graph[node]:
                if detectCycleDfs(n, visited, inStack):
                    return True
            # Remove the node from the stack.
            inStack[node] = False
            return False
        
        for i in range(numCourses):
            if detectCycleDfs(i, visited, inStack):
                return False
            
        return True
    
    def canFinishKhan(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses