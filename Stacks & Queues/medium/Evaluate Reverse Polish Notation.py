# 150
from math import ceil, floor
class Solution:
    def evalRPN(self, tokens):
        stk = []
        for t in tokens:
            if t in "+-*/":
                b, a = stk.pop(), stk.pop()

                if t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(a - b)
                elif t == "*":
                    stk.append(a * b)
                else:
                    division = float(a) / float(b)
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(t))

        value = stk[0]
        if isinstance(value, float) and int(value) == value:
            return int(value)
        else:
            return stk[0]

# Time Complexity: O(n)
# Space Complexity: O(n)    