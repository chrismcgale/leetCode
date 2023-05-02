class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, remain, curr, res):
            if remain == 0:
                # Deep copy of comb
                res.append(list(comb))
                return
            
            for next_curr in range(curr, len(candidates)):
                if next_curr > curr and candidates[next_curr] == candidates[next_curr - 1]:
                    continue
                    
                pick = candidates[next_curr]
                
                # We sorted increasing
                if remain - pick < 0:
                    break
                    
                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, res)
                
                comb.pop()
                
        candidates.sort()
        comb, res = [], []
        backtrack(comb, target, 0, res)

        return res
            