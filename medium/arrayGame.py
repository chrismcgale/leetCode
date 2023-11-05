class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        max_elem = max(arr)
        
        if k > n:
            return max_elem
        
        winner = arr[0]
        count = 0
        
        for i in range(1, n):
            
            if winner > arr[i]:
                count += 1
            else:
                count = 1
                winner = arr[i]
                
            if count == k or winner == max_elem:
                return winner