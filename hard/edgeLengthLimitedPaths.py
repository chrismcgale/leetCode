class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i
            
    def find(self, node: int):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def join(self, node1: int, node2: int):
        g1 = self.find(node1)
        g2 = self.find(node2)
        
        if g1 == g2:
            return
        
        if self.rank[g1] > self.rank[g2]:
            self.group[g2] = g1
        elif self.rank[g1] < self.rank[g2]:
            self.group[g1] = g2
        else:
            self.group[g1] = g2
            self.rank[g2] += 1
            
    def is_connected(self, node1: int, node2: int):
        return self.find(node1) == self.find(node2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        q_count = len(queries)
        ans = [False] * q_count
        
        q_with_ind = [[] for _ in range(q_count)]
        for i in range(q_count):
            q_with_ind[i] = queries[i]
            q_with_ind[i].append(i)
            
        edgeList.sort(key=lambda x: x[2])
        q_with_ind.sort(key=lambda x: x[2])
        
        edges_ind = 0
        
        for [p, q, limit, q_org_ind] in q_with_ind:
            while edges_ind < len(edgeList) and edgeList[edges_ind][2] < limit:
                node1 = edgeList[edges_ind][0]
                node2 = edgeList[edges_ind][1]
                uf.join(node1, node2)
                edges_ind += 1
                
            ans[q_org_ind] = uf.is_connected(p, q)
            
        return ans
        