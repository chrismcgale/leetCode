class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        
        # Recursively build the undirected graph from the given binary tree.
        def build_graph(cur, p):
            if cur and p:
                parent[cur.val] = p
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)
        
        answer = []
        visited = set([target.val])

        
        # Add the target node to the queue with a distance of 0
        queue = collections.deque([(target, 0)])
        while queue:
            cur, distance = queue.popleft()

            # If the current node is at distance k from target,
            # add it to the answer list and continue to the next node.
            if distance == k:
                answer.append(cur.val)
                continue

            # Add all unvisited neighbors of the current node to the queue.
            if cur.val in parent.keys() and parent[cur.val].val not in visited:
                visited.add(parent[cur.val].val)
                queue.append((parent[cur.val], distance + 1))
                
            if cur.left and cur.left.val not in visited:
                visited.add(cur.left.val)
                queue.append((cur.left, distance + 1))
                
            if cur.right and cur.right.val not in visited:
                visited.add(cur.right.val)
                queue.append((cur.right, distance + 1))
            
                    
        return answer