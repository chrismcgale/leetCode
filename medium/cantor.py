class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(str((int(nums[i][i]) + 1)  % 2))
               
        return "".join(ans)