class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        count, max_count = 0, 0
        
        for i, c in enumerate(s):
            if count == k:
                break

            if c in vowels:
                count += 1
            
            if i >= k and s[i - k] in vowels:
                count -= 1
                
            max_count = max(max_count, count)
                
        return max_count