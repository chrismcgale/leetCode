class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        heap = []
        res = ""
        for c in s:
            count[c] = count.get(c, 0) + 1
            
        for key, val in count.items():
            heappush(heap, (-val, key))
            
        while heap:
            val, key = heappop(heap)
            
            if not res or res[-1] != key:
                res += key
                if val + 1 != 0:
                    heapq.heappush(heap, (val + 1, key))       
            else:
                if not heap: return ""
                second_val, second_key = heappop(heap)
                res += second_key
                if second_val + 1 != 0:
                    heapq.heappush(heap, (second_val + 1, second_key))   
                heapq.heappush(heap, (val, key))
                
        return res
    
    def reorganizeStringOdds(self, s: str) -> str:
        char_count = Counter(s)
        max_count, letter = 0, ''
        for char, count in char_count.items():
            if count > max_count:
                max_count = count
                letter = char
        if max_count > (len(s) + 1) // 2:
            return ""
        ans = [''] * len(s)
        index = 0
        
        # Place the most frequent letter
        while char_count[letter] != 0:
            ans[index] = letter
            index += 2
            char_count[letter] -= 1

        # Place rest of the letters in any order
        for char, count in char_count.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)