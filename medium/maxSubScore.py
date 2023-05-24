class Solution:
    # Find non continuous subsequence of length k that yields best score
    # Score measured as sum(choose k from nums1) * max(Same k positions from nums2)
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
            
        # min heap to maintain top k elements
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        
        # score of first k pairs
        answer = top_k_sum * pairs[k - 1][1]
        
        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])
            
            answer = max(answer, top_k_sum * pairs[i][1])
            
        return answer