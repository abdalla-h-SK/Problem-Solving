# 1768

# my solution -> 

#   Time: O(m + n)
#   Space:O(m + n)
 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        output = ""
        idx = 0

        min_len_word = min(word1, word2, key = len)
        len_min = len(min_len_word)

        for i in range(len_min):
            new_word = "{}{}".format(word1[idx], word2[idx])
            output += new_word
            idx += 1

        if len(word1) > len(word2):
            output += word1[len(word2):]
        else:
            output += word2[len(word1):]

        return output

# another solution -> 

#   Time: O(m + n)
#   Space:O(m + n)

class Solution:
    def mergeAlternately(self, word1, word2):
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []

        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return ''.join(s)