# my solution ->

class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        greatest = -1

        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, temp)
        
        return arr