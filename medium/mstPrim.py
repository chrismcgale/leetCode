class Solution:
    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        edges_used = 0
        
        in_mst = [False] * n
        
        # min-heap
        heap = [(0, 0)]
        
        while edges_used < n:
            weight, curr = heapq.heappop(heap)
            
            if in_mst[curr]:
                continue
                
            in_mst[curr] = True
            mst_cost += weight
            edges_used += 1
            
            for next_node in range(n):
                if not in_mst[next_node]:
                    heapq.heappush(heap, (self.distance(points[curr], points[next_node]), next_node))
                         
        return mst_cost
    
    def minCostConnectPointsOptimized(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        edges_used = 0
        
        in_mst = [False] * n
        min_dist = [math.inf] * n
        min_dist[0] = 0
          
        while edges_used < n:
            curr_min_edge, curr = math.inf, -1
            
            # Pick least weight node which is not in MST.
            for node in range(n):
                if not in_mst[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr = node
                
            in_mst[curr] = True
            mst_cost += curr_min_edge
            edges_used += 1
            
            for next_node in range(n):
                if not in_mst[next_node]:
                    weight = self.distance(points[curr], points[next_node])
                    if not in_mst[next_node] and min_dist[next_node] > weight:
                        min_dist[next_node] = weight
                         
        return mst_cost