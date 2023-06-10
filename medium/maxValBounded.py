class Solution:
    def getSum(self, index, value, n) -> int:
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
            
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        
        return count - value
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        
        return lo