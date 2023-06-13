class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()
        
    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a]
        my_trie.count += 1
        
    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        # For each row
        for row in grid:
            # For each col
            for col in range(n):
                # For each item in that row see if it's equal to col index
                for i, r in enumerate(row):
                    if grid[i][col] != r:
                        break

                    if i == n - 1:
                        ans += 1
        return ans
    
    def equalPairsWithHash(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        row_counter = collections.Counter(tuple(row) for row in grid)
        
        # For each col add number of rows with same order
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            ans += row_counter[tuple(col)]
        
        return ans
    
    def equalPairsWitTrie(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        n = len(grid)
        ans = 0
        for row in grid:
            my_trie.insert(row)
        
        # For each col add number of rows with same order
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            ans += my_trie.search(tuple(col))
        
        return ans
    
    