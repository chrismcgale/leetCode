class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        
        if s == goal:
            # If we have 2 same characters in string 's',
            # we can swap them and still the strings will remain equal.
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
                if count[ord(ch) - ord('a')] == 2:
                    return True
            # Otherwise, if we swap any two characters, it will make the strings unequal.
            return False
        
        n = len(s)
        
        diff, i, j = 0, -1, -1
        
        for k in range(n):
            if s[k] != goal[k]:
                diff += 1
                if diff == 1:
                    i = k
                elif diff == 2:
                    j = k
                else:
                    return False
        
        return diff == 2 and s[i] == goal[j] and s[j] == goal[i]