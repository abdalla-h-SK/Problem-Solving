# 985
# my solution ->

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        cur = 0
        for num in nums:
            if not num % 2:
                cur += num

        ans = []

        for add, i in queries:
            if not nums[i] % 2:
                if not add % 2:
                    cur += add
                else:
                    cur -= nums[i]
            else:
                if add % 2:
                    cur += (nums[i] + add)

            nums[i] += add
            ans.append(cur)
        
        return ans