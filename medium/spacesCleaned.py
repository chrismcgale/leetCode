class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        ans = 1
        rows, cols = len(room), len(room[0])
        
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        room[0][0] = -1
        key = 0
        
        curr_y, curr_x = 0, 0
        direct_x, direct_y = direct[key]
        seen = set()

        while (curr_x, curr_y, key) not in seen:
            seen.add((curr_x, curr_y, key))
            next_row, next_col = curr_y + direct_y, curr_x + direct_x
            if 0 <= next_row < rows and 0 <= next_col < cols and room[next_row][next_col] != 1:
                curr_y, curr_x = next_row, next_col
                
                if room[next_row][next_col] == 0:
                    ans += 1
                    room[next_row][next_col] = -1
                    
            else:
                key = (key + 1) % 4
                direct_x, direct_y = direct[key]
                   
        return ans