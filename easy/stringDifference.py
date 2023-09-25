class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = {}
        t_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
            
        for d in t:
            t_map[d] = t_map.get(d, 0) + 1
            
        for k, v in t_map.items():
            if v != s_map.get(k, 0):
                return k
            
        return ""
    
    def findTheDifferenceBit(self, s: str, t: str) -> str:
        ch = 0
        
        # XORs cancel out and the difference is whats left over
        for c in s:
            ch ^= ord(c)
            
        for d in t:
            ch ^= ord(d)
            
        return chr(ch)