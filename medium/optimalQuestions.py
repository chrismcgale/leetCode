class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        
        for i in range(n - 2, -1, -1):
            q = questions[i]
            if i + q[1] + 1 < n:
                dp[i] = max(dp[i + 1], q[0] + dp[i + q[1] + 1])
            elif i < n - 1:
                dp[i] =  max(dp[i + 1], q[0])
            else:
                dp[i] = q[0]
            

        return dp[0]