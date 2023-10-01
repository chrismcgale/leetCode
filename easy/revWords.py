class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        ans = ""
        for c in s:
            if c == " ":
                ans += "".join(stack)[::-1] + " "
                stack = []
            else:
                stack.append(c)
                
        ans += "".join(stack)[::-1]
        return ans