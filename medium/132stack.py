class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])
            
        for i in range(len(nums) -1, -1, -1):
            if nums[i] <= min_array[i]:
                continue
                
            while stack and stack[-1] <= min_array[i]:
                stack.pop()
            
            if stack and stack[-1] < nums[i]:
                return True
            
            stack.append(nums[i])
            
        return False