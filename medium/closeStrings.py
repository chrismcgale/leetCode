from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count1, count2 = Counter(word1), Counter(word2)
        
        for k in count1:
            if k not in count2:
                return False
        
        arr1, arr2 = list(count1.values()), list(count2.values())
        
        arr1.sort()
        arr2.sort()
            
        return arr1 == arr2