# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = head
        for i in range(k - 1):
            begin = begin.next
            
        forw = begin
        end = head
        
        while forw.next:
            forw = forw.next
            end = end.next

            
        temp = begin.val
        begin.val = end.val
        end.val = temp
        
        return head