# 228

# my solution ->

#   time : O(n)
#   space: O(n)

class Solution(object):
    def summaryRanges(self, nums):
        output = []
        if not nums:
            return []
        current = nums[0]

        for i in range(len(nums)):
            con = ("{}->{}".format(current, nums[i]))

            if current == nums[-1]:
                output.append(str(current))
                break
            if i != len(nums) - 1:
                if nums[i] + 1 == nums[i + 1]:
                    continue
                else:
                    if current == nums[i]:
                        output.append(str(current))
                        current = nums[i + 1]
                    else:
                        output.append(con)
                        current = nums[i + 1]
            else:
                output.append(con)
        return output

# another solution ->

#   time : O(n)
#   space: O(n)

class Solution:
    def summaryRanges(self, nums):
        ans = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ans.append(str(start) + "->" + str(nums[i]))
            else: 
                ans.append(str(nums[i]))
            
            i += 1

        return ans