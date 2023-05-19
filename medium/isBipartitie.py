class Solution:
    # Graph is biartite iff there is a 2 coloring
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}
        
        for i in range(n):
            if i not in color:
                stack = [i]
                color[i] = 0

                while stack:
                    node = stack.pop()
                    for neigh in graph[node]:
                        if neigh not in color:
                            color[neigh] = color[node] ^ 1
                            stack.append(neigh)
                        elif color[node] == color[neigh]:
                            return False

        return True