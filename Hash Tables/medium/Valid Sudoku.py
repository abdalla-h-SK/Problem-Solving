# 36
# my solution ->

#   Time : O(1) , Space : O(1)

class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] in nums:
                    return False

                if board[i][j].isdigit():
                    nums.add(board[i][j])
        
        for j in range(9):
            nums = set()
            for i in range(9):
                if board[i][j] in nums:
                    return False
                
                if board[i][j].isdigit():
                    nums.add(board[i][j])
        
        for box in range(9):
            rows = box // 3
            cols = box % 3
            start_row = cols * 3
            start_col = rows * 3
            nums = set()

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] in nums:
                        return False

                    if board[i][j].isdigit():
                        nums.add(board[i][j])
        
        return True