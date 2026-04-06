# 155

# my solution ->

#   Time : O(1)
#   Space: O(n)

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, val):
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.minStack.append(self.min)

    def pop(self):
        temp = self.stack.pop()
        if temp == self.min:
            self.minStack.pop()
            if not self.minStack:
                self.min = float('inf')
            else:
                self.min = self.minStack[-1]

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        return None
    

# another solution ->

class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val):
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self):
        self.stk.pop()
        self.min_stk.pop()

    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.min_stk[-1]

# Time Complexity: O(1)
# Space Complexity: O(n)