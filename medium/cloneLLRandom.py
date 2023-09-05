"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.mapping = {}
        
    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the mapping dictionary          
            if node in self.mapping:
                # If its in the mapping dictionary then return the new node reference from the dictionary
                return self.mapping[node]
            else:
                # Otherwise create a new node, save the reference in the mapping dictionary and return it.
                self.mapping[node] = Node(node.val, None, None)
                return self.mapping[node]
        return None
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        prev = head
        new_node = Node(head.val, None, None)
        self.mapping[prev] = new_node

        while prev:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(prev.random)
            new_node.next = self.getClonedNode(prev.next)

            # Move one step ahead in the linked list.
            prev = prev.next
            new_node = new_node.next

        return self.mapping[head]