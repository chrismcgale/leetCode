class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right, ans = [], []
        
        for a in asteroids:
            if a > 0:
                right.append(a)
            else:
                # Check if a is not destroyed
                flag = True
                
                while right:
                    # Larger asteriods
                    if right[-1] > abs(a):
                        flag = False
                        break
                        
                    # Same size
                    if right[-1] == abs(a):
                        flag = False
                        right.pop()
                        break
                    right.pop()
                    
                if flag:
                    ans.append(a) 
                    
        ans += right
        return ans