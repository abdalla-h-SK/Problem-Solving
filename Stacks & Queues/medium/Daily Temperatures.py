# 739

# chat Gpt solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx 
            stack.append(i)

        return answer