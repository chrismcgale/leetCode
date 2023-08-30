class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        curr_l = 0
        for w in words:
            # new line needed
            if len(w) + curr_l + len(curr) > maxWidth:
                
                spaces_to_add = maxWidth - curr_l
                if len(curr) == 1:
                    res.append(curr[0] + " " * spaces_to_add)
                else:
                    spaces_per = spaces_to_add // (len(curr) - 1)

                    for i in range(spaces_to_add - (spaces_per * (len(curr) - 1))):
                        curr[i] += " "

                    res.append((" " * spaces_per).join(curr))
                curr = []
                curr_l = 0
                
            curr.append(w)
            curr_l += len(w)
            
        if curr:
            spaces_to_add = maxWidth - (curr_l + len(curr) - 1)
            res.append((" ").join(curr) + " " * spaces_to_add)
            
        return res
            