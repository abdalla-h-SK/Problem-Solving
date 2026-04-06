# 20

class Solution(object):
    def isValid(self, s):
        stack = []
        for item in s:
            if item in {'}', ')', ']'}:
                if stack:
                    if item == '}' and stack[-1] == '{':
                        stack.pop()
                    elif item == ')' and stack[-1] == '(':
                        stack.pop()
                    elif item == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(item)

        return len(stack) == 0
    
#   Time : O(n)
#   Space: O(n)