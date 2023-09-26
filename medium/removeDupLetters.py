class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        pos = 0
        
        # Find the smallest character such that its suffix contains at least one copy of every character in the string
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0: break
        
        # Recursively do rest of answer
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''
    
    
    def removeDuplicateLettersStack(self, s: str) -> str:
        stack = []
        
        # this lets us keep track of what's in our solution in O(1) time
        seen = set()
        
         # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        # we can only try to add c if it's not already in our solution
        # this is to maintain only one of each character
        for i, c in enumerate(s):
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
                
        return ''.join(stack)