class Solution:    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        max_speed = 10 ** 7
        lo, hi = 1, max_speed
        
        # Last one can be a partial hour trip length
        def onTime(speed):
            return sum(math.ceil(d / speed) for d in dist[:-1]) + dist[-1] / speed <= hour
        
        while lo < hi:
            m = lo + (hi - lo) // 2
            
            if not onTime(m):
                lo = m + 1
            else: 
                hi = m
                
        if lo == max_speed and not onTime(lo):
            return -1
        
        return lo