# 1942
# my solution ->

class Solution(object):
    def kthFactor(self, n, k):

        factors = []

        for i in range(1, (n // 2) + 1):
            is_factor = n % i
            if is_factor == 0:
                factors.append(i)
            
        factors.append(n)

        return factors[k-1] if k <= len(factors) else -1