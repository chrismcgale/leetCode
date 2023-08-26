class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        
        curr = float('-inf')
        res = 0
        
        for p in pairs:
            if p[0] > curr:
                res += 1
                curr = p[1]
        
        return res