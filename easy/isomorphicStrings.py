class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        used = {}
        
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            elif t[i] in used:
                return False
            else:
                hashmap[s[i]] = t[i]
                used[t[i]] = True
                
        return True