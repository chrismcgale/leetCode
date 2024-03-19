class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        ans = 0
        
        for i in tasks:
            freq[ord(i) - ord('A')] += 1
            
        freq_list = [-f for f in freq if f > 0]

        heapify(freq_list)
               
        while freq_list:
            cycle = n + 1
            store = []
            task_count = 0
            
            # Pop top until you go through n cycles
            while cycle > 0 and freq_list:
                curr_freq = -heappop(freq_list)
                if curr_freq > 1:
                    store.append(-(curr_freq - 1))
                task_count += 1
                cycle -= 1
                
            # If you stored any add back to heap
            for x in store:
                heappush(freq_list, x)
                
            ans += task_count if not freq_list else n + 1
            
        return ans