# 215
# my solution ->

# Time : O(n + k log(n))
# Space: O(1)

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        ans = None

        for i in range(k):
            ans = heapq.heappop(nums)
            
        return -ans


# another solution ->

# Time : O(n log(k))
# Space: O(n)

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        
        return heap[0]


# the deterministic selection worked here but the quickselection didn't !

# my solution ->  Time : O(n) , Space : O(n)

class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]

        def median_of_medians(arr):
            if len(arr) <= 5:
                return sorted(arr)[len(arr) // 2]
            sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
            medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
            return median_of_medians(medians)

        def partition(arr, pivot):
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return left, middle, right

        def deterministic_select(arr, k):
            pivot = median_of_medians(arr)
            left, middle, right = partition(arr, pivot)
            if k < len(left):
                return deterministic_select(left, k)
            elif k < len(left) + len(middle):
                return middle[0]
            else:
                return deterministic_select(right, k - len(left) - len(middle))

        result = deterministic_select(nums, k-1)
        return -result