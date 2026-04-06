# 380
# ChatGpt!

import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val):
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        index = self.indices[val]
        last_element = self.nums[-1]

        self.nums[index] = last_element
        self.indices[last_element] = index

        self.nums.pop()
        del self.indices[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)