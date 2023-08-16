class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            res.append(nums[dq[0]])
            
        return res
    
    def maxSlidingWindowPQ(self, nums: List[int], k: int) -> List[int]:
        res = []
        pq = [(-nums[i], i) for i in range(k)]
        
        heapq.heapify(pq)
        res.append(-pq[0][0])
        
        s = 0
        for i in range(k, len(nums)):
            s += 1
            
            while pq and pq[0][1] < s:
                heappop(pq) 
           
            heapq.heappush(pq, (-nums[i], i))
            res.append(-1 * pq[0][0])
            
        return res