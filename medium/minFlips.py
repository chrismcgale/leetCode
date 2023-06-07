class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if (c % 2) != (a % 2 or b % 2):
                if c % 2 == 0 and a % 2 and b % 2:
                    ans += 2
                else:
                    ans += 1
                
            c //= 2
            a //= 2
            b //= 2
        return ans