class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def solve(one, two):
            if one == two:
                return 0
            
            if len(one) == 0:
                return sum(ord(c) for c in two)
            
            if len(two) == 0:
                return sum(ord(c) for c in one)
            
            if one[0] == two[0]:
                return solve(one[1:], two[1:])
            
            return min(min(ord(one[0]) + solve(one[1:], two), ord(two[0]) + solve(one, two[1:])), ord(one[0]) + ord(two[0]) + solve(one[1:], two[1:]))
            
        return solve(s1, s2)