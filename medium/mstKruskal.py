class UnionFind:
    def __init__(self, n):
        self.group = [0] * n
        self.rank = [0] * n
        
        for i in range(n):
            self.group[i] = i
        
    def find(self, a):
        if self.group[a] != a:
            self.group[a] = self.find(self.group[a])
        return self.group[a]
        
    def join(self, a, b):
        group1 = self.find(a)
        group2 = self.find(b)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True


class Solution:
    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        edges_used = 0
        
        uf = UnionFind(n)
        all_edges = []
        
        # Construct all edges
        for p in range(n):
            for q in range(p + 1, n):
                all_edges.append((self.distance(points[p], points[q]), p, q))
        
        # Sort edges
        all_edges.sort()
        
        for weight, n1, n2 in all_edges:
            if uf.join(n1, n2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
                         
        return mst_cost