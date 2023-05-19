class Solution:
    # Works but time mem limit exceeded for long strings
    def longestDPPalindrome(self, s: str) -> str:  
        n = len(s)
        start, end = 0, 0
        
        @cache
        def solve(i, j):
            if j == i:
                return True
            
            if j == i + 1:
                return s[j] == s[i]
            
            if s[i] == s[j] and solve(i + 1, j - 1):
                return True
            else:
                return False
            
        
        for i in range(n):
            for j in range(i, n):
                if solve(i, j) and j - i + 1 > end:
                    start = i
                    end = j - i + 1
        
        return s[start : start + end]
    
    def longestPalindrome(self, s: str) -> str:  
        n = len(s)
        start, end = 0, 0
        
        @cache
        def solve(i, j):
            L, R = i, j
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
                
            return R - L - 1  
        
        for i in range(n):
            l1, l2 = solve(i, i), solve(i, i + 1)
            m = max(l1, l2)
            if m > end - start:
                start = i - (m - 1) // 2
                end = i + m // 2
        
        return s[start : end + 1]
                