# 657
# my solution ->

class Solution(object):
    def judgeCircle(self, moves):
        origin = 0
        moves_dict = {'U':1, 'D':-1, 'R':1j, 'L':-1j}

        dictionary = {'U', 'D', 'R', 'L'}
        for move in moves:
            if move in dictionary:
                origin += moves_dict[move]
        
        return origin == 0