class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A, B = 0, 0
        if len(colors) < 3:
            return False
        
        ago, last = colors[0], colors[1]
        for c in colors[2:]:
            if c == last == ago:
                if c == "A":
                    A += 1
                else:
                    B += 1
            
            ago = last
            last = c
            
        return A > B