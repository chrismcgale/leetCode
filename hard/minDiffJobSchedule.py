class Solution(object):
    # Top down DP
    def minBUDifficulty(self, jobDifficulty: List[int], d: int):
        n = len(jobDifficulty)
        
        if n < d:
            return -1
        
        max_job_remaining = jobDifficulty[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])
            
        @cache
        def min_diff(i, days_remain):
            if days_remain == 1:
                return max_job_remaining[i]
            
            res = float('inf')
            daily_max_diff = 0
            
            for j in range(i, n - days_remain + 1):
                daily_max_diff = max(daily_max_diff, jobDifficulty[j])
                res = min(res, daily_max_diff + min_diff(j + 1, days_remain - 1))
                
            return res
        
        return min_diff(0, d)
    
    # Botton up DP
    def minTDDifficulty(self, jobDifficulty: List[int], d: int):
        n = len(jobDifficulty)
        
        min_diff_next_day = [float('inf')] * n + [0]
        
        for days_remain in range(1, d + 1):
            min_diff_curr_day = [float('inf')] * n + [0]
            for i in range(n - days_remain + 1):
                daily_max_diff = 0
                for j in range(i + 1, n - days_remain + 2):
                    daily_max_diff = max(daily_max_diff, jobDifficulty[j - 1])
                    min_diff_curr_day[i] = min(min_diff_curr_day[i], daily_max_diff + min_diff_next_day[j])
            min_diff_next_day = min_diff_curr_day
            
        return min_diff_next_day[0] if min_diff_next_day[0] < float('inf') else -1