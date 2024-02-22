class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound, outbound = {}, {}
        
        for pairs in trust:
            outbound[pairs[0]] = outbound.get(pairs[0], 0) + 1
            inbound[pairs[1]] = inbound.get(pairs[1], 0) + 1
            
        for i in range(1, n + 1):
            if outbound.get(i, 0) == 0 and inbound.get(i, 0) == n - 1:
                return i
            
        return -1