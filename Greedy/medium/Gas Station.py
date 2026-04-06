# 134
# my solution -> Why I make every thing COMPLIX!

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        increase = False
        prev, cur, last_increament = None, gas[0] - cost[0], [None, 0]

        for i in range(1, len(gas)):
            prev = cur

            cur += gas[i]
            cur -= cost[i]

            if cur < prev and increase:
                last_increament[0] -= (prev - cur)

                if last_increament[0] < 0:
                    last_increament = [None, 0]
                    increase = False
                
            elif cur > prev:
                if increase:
                    last_increament[0] += (cur - prev)
                else:
                    increase = True
                    last_increament = [cur - prev, i]

        return last_increament[1] if cur >= 0 else -1


# another solution -> It was very clear!

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        in_hand, required = sum(gas), sum(cost)
        if in_hand < required:
            return -1
        
        total = last_increase = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:

                total = 0
                last_increase = i + 1
        
        return last_increase