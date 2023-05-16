class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Acts as prev for head node
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Prep for next iteration
            prev = first
            head = first.next
            
                
        return dummy.next
        
    def swapPairsRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not(head and head.next): return head 

        newHead = head.next
        head.next, newHead.next = self.swapPairsRecur(head.next.next), head

        return newHead