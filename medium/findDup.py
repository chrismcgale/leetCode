class Solution:
    def sorting(self, nums: List[int]) -> int:
        nums.sort()
        last = nums[1]
        
        for i in nums:
            if i == last:
                return i
            
            last = i
            
    def negMarking(self, nums: List[int]) -> int:        
        for i in nums:
            cur = abs(i)
            if nums[cur] < 0:
                dup = cur
                break
            nums[cur] = -nums[cur]
            
        for j in range(len(nums)):
            nums[j] = abs(nums[j])
            
        return dup
    
    def tortoiseHare(self, nums: List[int]) -> int:
        tort = hare = nums[0]
        
        while True:
            tort, hare = nums[tort], nums[nums[hare]]
            if tort == hare:
                break
            
        tort = nums[0]
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]
    
        return hare