class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        combs = []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if index == len(digits):
                combs.append("".join(path))
                return # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Move on to the next digit
                backtrack(index + 1, path + [letter])
                
        backtrack(0, [])
        return combs