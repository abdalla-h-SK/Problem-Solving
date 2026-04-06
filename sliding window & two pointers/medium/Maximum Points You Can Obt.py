# 1423
# my solution ->

class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        sum_cards = 0
        for i in range(n - k):
            sum_cards += cardPoints[i]
        
        min_sum = sum_cards
        for i in range(n - k, n):
            sum_cards += cardPoints[i]
            sum_cards -= cardPoints[i - (n - k)]

            min_sum = min(min_sum, sum_cards)
        
        return sum(cardPoints) - min_sum