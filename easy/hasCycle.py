class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False 
        
        single, double = head, head.next
        
        while double and double.next and double.next.next and single and single.next:
            if single == double:
                return True
            
            single = single.next
            double = double.next.next
            
        return False
    
    def hasCycleSet(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False