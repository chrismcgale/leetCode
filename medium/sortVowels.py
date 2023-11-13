class Solution:
    def isVowel(self, ch): 
        la=[97,101,105,111,117] 
        ua=[65,69,73,79,85] 
        
        if ord(ch) in la or ord(ch) in ua: 
            return True
        return False
    
    def sortVowels(self, s: str) -> str:
        l = list(s)
        vowels = []
        pos = []
        
        for i, c in enumerate(l):
            if self.isVowel(c):
                vowels.append(c)
                pos.append(i)
                
        vowels.sort()
        
        for i, p in enumerate(pos):
            l[p] = vowels[i]
            
        return "".join(l)
        