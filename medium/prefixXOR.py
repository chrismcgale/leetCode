class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        x = 0

        for i in pref:
            x ^= i
            res.append(x)
            x ^= x ^ i
        
        return res