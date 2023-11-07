class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_until_reached = [dist[i] / speed[i] for i in range(n)]
        
        time_until_reached.sort()
        
        ans = 0
        
        while ans < n:
            if time_until_reached[ans] - ans <= 0:
                break
            ans += 1
            
        return ans