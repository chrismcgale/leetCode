class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_empty = 0
        curr = 0
        res = 0
        
        for i in range(len(customers)):
            curr += -1 if customers[i] == 'Y' else 1
            
            if curr < min_empty:
                res = i + 1
                min_empty = curr
            
        return res