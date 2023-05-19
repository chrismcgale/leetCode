class Solution:
    class Node:
        def __init__(self, char):
            self.char = char
            self.next = {}
            self.count = 0
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        head = self.Node("%")
        for s in strs:
            if s == "":
                return ""
            curr = head
            for c in s:
                # Add new char to next
                if c not in curr.next:
                    curr.next[c] = self.Node(c)
                    curr.count += 1
                curr = curr.next[c]
            # Note end of word
            curr.next["*"] = self.Node("*")
            curr.count += 1
                
        # Construct answer
        ans = ""
        while head.count == 1:
            c = list(head.next.keys())[0]
            if c == "*":
                break;
            ans += c
            head = head.next[c]
        return ans