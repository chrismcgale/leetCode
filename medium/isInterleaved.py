class Solution:
    def isInterleaveBU(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        n = len(s3)
        
        @lru_cache
        def inter(l, r):
            if l + r == n:
                return True
            
            left, right = False, False
            if l < len(s1) and s1[l] == s3[l + r]:
                left = inter(l + 1, r)
                
            if r < len(s2) and s2[r] == s3[l + r]:
                right = inter(l, r + 1)
            
            return left or right
        
        return inter(0, 0)

    def isInterleaveTD(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]       
        
        for l in range(len(s1) + 1):
            for r in range(len(s2) + 1):
                if l == 0 and r == 0:
                    dp[l][r] = True
                elif l == 0:
                    dp[l][r] = (dp[l][r - 1] and s2[r - 1] == s3[l + r - 1])
                elif r == 0:
                    dp[l][r] = (dp[l - 1][r] and s1[l - 1] == s3[l + r - 1])
                else:
                    dp[l][r] = (dp[l - 1][r] and s1[l - 1] == s3[l + r - 1]) or (dp[l][r - 1] and s2[r - 1] == s3[l + r - 1])
                    
                
        return dp[len(s1)][len(s2)]
    
    def isInterleaveTDBetterSpace(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [False for _ in range(len(s2) + 1)]
        
        for l in range(len(s1) + 1):
            for r in range(len(s2) + 1):
                if l == 0 and r == 0:
                    dp[r] = True
                elif l == 0:
                    dp[r] = (dp[r - 1] and s2[r - 1] == s3[l + r - 1])
                elif r == 0:
                    dp[r] = (dp[r] and s1[l - 1] == s3[l + r - 1])
                else:
                    dp[r] = (dp[r] and s1[l - 1] == s3[l + r - 1]) or (dp[r - 1] and s2[r - 1] == s3[l + r - 1])      
                    
                    
        return dp[len(s2)]
            