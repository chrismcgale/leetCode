class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        
        g.sort()
        s.sort()
        
        j = 0
        for i in range(len(s)):
            if j == len(g):
                break

            if g[j] <= s[i]:
                ans += 1
                j += 1
                
        return ans