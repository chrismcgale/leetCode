class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        n = len(s1)
        
        diff, i, j = 0, -1, -1
        
        for k in range(n):
            if s1[k] != s2[k]:
                diff += 1
                if diff == 1:
                    i = k
                elif diff == 2:
                    j = k
                else:
                    return False
        
        return diff == 2 and s1[i] == s2[j] and s1[j] == s2[i]