# 12
# my solution ->

class Solution(object):
    def intToRoman(self, num):
        one_five_map_inverted = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        four_nine_map_inverted = {4:'VI', 9:'XI', 40:'LX', 90:'CX', 400:'DC', 900:'MC'}

        d_inverted = {1:[1], 2:[1, 1], 3:[1, 1, 1], 5:[5], 
        6:[1, 5], 7:[1, 1, 5], 8:[1, 1, 1, 5], 10:[10]}

        ans, cell = '', 1

        while num != 0:
            pick = num % 10
            num //= 10

            if pick * cell in four_nine_map_inverted:
                ans += four_nine_map_inverted[pick * cell]
            elif pick in d_inverted:
                concat = d_inverted[pick]
                for i in concat:
                    ans += one_five_map_inverted[i * cell]

            cell *= 10
        
        return ans[::-1]
    

# another solution ->

class Solution(object):
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        for i in range(len(val)):
            while num >= val[i]:
                roman += symbols[i]
                num -= val[i]
        
        return roman