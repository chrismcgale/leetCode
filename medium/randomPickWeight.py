class Solution:
    def __init__(self, w: List[int]):
        self.con = []
        self.ln = len(w)
        pre_sum = 0
        for i in w:
            pre_sum += i
            self.con.append(pre_sum)
        self.sum = pre_sum
        

    def pickIndex(self) -> int:
        pick = self.sum * random.random()
        lo, hi = 0, self.ln
        
        while lo < hi:
            m = lo + (hi - lo) // 2
            if (m > 0 and self.con[m - 1] < pick) and (self.ln and pick <= self.con[m]):
                return m
            
            if m == 0 or m == self.ln:
                return m
            
            if self.con[m] < pick:
                lo = m
            elif self.con[m] > pick:
                hi = m