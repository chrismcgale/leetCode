class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}
        
        freq[0] = 1
        
        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - 97      
            
            mask ^= (1 << bit)
            
            res += freq.get(mask, 0)
            
            freq[mask] = freq.get(mask, 0) + 1
            
            # Only chars a - j
            for odd_c in range(10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]

        return res