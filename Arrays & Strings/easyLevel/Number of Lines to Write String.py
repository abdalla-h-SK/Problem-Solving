# 806
# my solution ->

class Solution(object):
    def numberOfLines(self, widths, s):
        n = len(s)
        lines = 1
        width = 0

        for i in s:
            index = ord(i) - 97
            if width + widths[index] <= 100:
                width += widths[index]
            else:
                lines += 1
                width = widths[index]
        
        return [lines, width]