class Solution:
    def binarySearch(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        if len(intervals) == 0:
            return 0
        
        lo, hi = 0, len(intervals) - 1
        ans = len(intervals)
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if intervals[mid][0] > newInterval[0]:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
                 
        return ans
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        ans = []
        
        upper = self.binarySearch(intervals, newInterval)
        
        intervals = intervals[:upper] + [newInterval] + intervals[upper:]

        i = 0
        while i < len(intervals):
            insertInt = intervals[i]
            while i < len(intervals) and min(insertInt[1], intervals[i][1]) >= max(insertInt[0], intervals[i][0]):
                insertInt = [min(insertInt[0], intervals[i][0]), max(insertInt[1], intervals[i][1])]
                i += 1
            
            ans.append(insertInt)
            
        return ans