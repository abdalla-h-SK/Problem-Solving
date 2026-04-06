# 68

# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def fullJustify(self, words, maxWidth):

        output = []
        while words:
            curr_ln = 0
            actual_ln = 0
            lst = []
            curr_sentense = ''
            while curr_ln + len(words[0]) <= maxWidth:
                lst.append(words[0])
                curr_ln += len(words[0]) + 1
                actual_ln += len(words[0])
                words.pop(0)
                if not words:
                    break   
                
            num_spaces = len(lst) - 1
            left_space = maxWidth - actual_ln
            if num_spaces == 0:
                curr_sentense += lst[0] + left_space * ' '
                output.append(curr_sentense)
                continue

            tps = left_space // num_spaces
            ad_tps = left_space % num_spaces

            while lst:
                if not words:
                    if len(lst) == 1:
                        curr_sentense += lst[0]
                    else:
                        curr_sentense += lst[0] + ' '
                    lst.pop(0)

                    if not lst:
                        curr_ln -= 1
                        curr_sentense += (maxWidth - curr_ln) * ' '
                        output.append(curr_sentense)
                        return output

                elif ad_tps:
                    curr_sentense += lst[0] + (tps + 1) * ' '
                    ad_tps -= 1
                    lst.pop(0)
                else:
                    if len(lst) == 1:
                        curr_sentense += lst[0]
                    else:
                        curr_sentense += lst[0] + tps * ' '
                    lst.pop(0)

            output.append(curr_sentense)
        
        return output