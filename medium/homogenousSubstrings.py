class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        streak = 0
        ans = 0
        
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                streak += 1
                
            else:
                streak = 1

            ans = (ans + streak) % mod
            
        return ans