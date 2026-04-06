# 225

# mu solution -> That took so long and its implementation takes too long but I'm satisfied

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def calculate(self, s):
        stack = []
        num = ''
        signs = {'+', '-'}

        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
                if i == len(s) - 1:
                    stack.append(int(num))
                else:
                    if s[i + 1].isdigit():
                        continue
                    else:
                        stack.append(int(num))
                        
                        num = ''
            else:
                if s[i] in signs and len(stack) == 0:
                    num += s[i]
                    continue
                elif s[i] in signs and type(stack[-1]) is not int:
                    num += s[i]
                    continue
                elif s[i] != ')' and s[i] != ' ':
                    if num and not s[i].isdigit():
                        stack.append(num)
                        num = ''
                    stack.append(s[i])


            while len(stack) > 1:

                if s[i] == ')':
                    stack.pop(-2)
                if len(stack) == 1:
                    continue

                if stack[-2] == '+' and stack[-1] != '(':
                    if len(stack) == 2:
                        stack.pop(0)
                        break

                    elif len(stack) > 2 and type(stack[-3]) is not int:
                        stack.pop(-2)
                        break
                
                    y = stack.pop()
                    stack.pop()
                    x = stack.pop()
                    stack.append(x + y)
                elif stack[-2] == '-' and stack[-1] != '(':
                    if len(stack) == 2:
                        stack.pop(0)
                        stack[0] = - stack[0]
                        break

                    elif len(stack) > 2 and type(stack[-3]) is not int:
                        stack.pop(-2)
                        stack[-1] = - stack[-1]
                        break

                    y = stack.pop()
                    stack.pop()
                    x = stack.pop()
                    stack.append(x - y)
                else:
                    break
                
                if s[i] == ')':
                    break

        return stack[0]


# another solution -> 

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def calculate(self, s):

        stack = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == "+":
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ")":
                res += sign * operand
                sign = stack.pop()
                res *= sign
                res += stack.pop()
                operand = 0
        return res + sign * operand