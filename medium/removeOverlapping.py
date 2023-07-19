class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end
        intervals.sort(key = lambda x: x[1])
        ans = 0
        
        last = intervals[0][1]
        
        for x, y in intervals[1:]:
            if x >= last:
                last = y
            else:
                ans += 1
            
        return ans