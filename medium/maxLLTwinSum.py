class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        m = 0
        
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        full = len(stack)
        half = full // 2
        curr = head
            
        for i in range(half):
            m = max(m, curr.val + stack.pop())
            curr = curr.next
        
        return m