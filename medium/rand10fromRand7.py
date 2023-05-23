class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 0
        
        while True:
            row = rand7()
            col = rand7()
            idx = col + (row - 1) * 7
            if idx <= 40:
                break
                
        return 1 + (idx - 1) % 10
    
    def fastRand10(self):
        """
        :rtype: int
        """
        idx = 0
        while True:
            a = rand7()
            b = rand7()
            idx = a + (b - 1) * 7
            if idx <= 40:
                break
            
            a = idx - 40
            b = rand7()
            idx = a + (b - 1) * 7
            if idx <= 60:
                break
            
            a = idx - 60
            b = rand7()
            idx = a + (b - 1) * 7
            if idx <= 20:
                break
                
        return 1 + (idx - 1) % 10
    
    