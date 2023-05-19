class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        doubles = 0
        
        for c in s:
            if c not in mp:
                mp[c] = 1
            elif mp[c] == 0:
                mp[c] += 1
            else:
                mp[c] = 0
                doubles += 1
                
        return doubles * 2 + (1 if doubles * 2 < len(s) else 0)