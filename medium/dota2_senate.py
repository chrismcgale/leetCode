class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        r_count = senate.count('R')
        d_count = len(senate) - r_count
        
        d_float_ban, r_float_ban = 0, 0
        
        q = deque(senate)
        
        while r_count and d_count:
            curr = q.popleft()
            
            if curr == 'D':
                if d_float_ban:
                    d_float_ban -= 1
                    d_count -= 1
                else:
                    r_float_ban += 1
                    q.append('D')
            else:
                if r_float_ban:
                    r_float_ban -= 1
                    r_count -= 1
                else:
                    d_float_ban += 1
                    q.append('R')
                    
        return 'Radiant' if r_count  else 'Dire'