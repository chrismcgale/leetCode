class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        freq_list = Counter(s)
        
        freq_list = [(key, freq_list[key]) for key in freq_list]
        
        freq_list.sort(key=lambda x: -x[1])
        
        max_freq_allowed = len(s)
        
        for key, freq in freq_list:
            if freq > max_freq_allowed:
                ans += freq - max_freq_allowed
                freq = max_freq_allowed
                
            max_freq_allowed = max(0, freq - 1)
        
        return ans