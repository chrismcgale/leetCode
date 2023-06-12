class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        if len(ranges) == 0:
            return [[0, n - 1]]
        
        ans = []
        
        # Sort by start
        ranges.sort()
        
        # Do 0 range
        if ranges[0][0] != 0:
            ans.append([0, ranges[0][0] - 1])
            
        m = ranges[0][1]
        
        # Find gaps in ranges
        for i, r in enumerate(ranges[1:]):
            if r[0] > m + 1:
                ans.append([m + 1, r[0] - 1])
        
            m = max(m, r[1])
        
        # Final range
        if m < n - 1:
            ans.append([m + 1, n - 1])
        
        return ans