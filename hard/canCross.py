class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        index = {}
        
        for i, rock in enumerate(stones):
            index[rock] = i
        
        @cache
        def jump(i, last_jump) -> bool:
            if i == n - 1:
                return True
            
            short = stones[i] + last_jump - 1
            same = stones[i] + last_jump
            far = stones[i] + last_jump + 1

            return (last_jump > 1 and short in index and jump(index[short], last_jump - 1)) or (last_jump > 0 and same in index and jump(index[same], last_jump)) or (far > 0 and far in index and jump(index[far], last_jump + 1))
            
            
        return jump(0, 0)