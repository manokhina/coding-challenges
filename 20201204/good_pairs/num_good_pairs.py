"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums):
        num_pairs = 0
        if len(nums) < 2:
            return num_pairs
        counter = Counter(nums)
        # repeated_counter = dict(filter(lambda elem: elem[1] > 1, counter.items()))
        for val in counter.values():
            if val > 1:
                num_pairs += self.combinations(val)
        return int(num_pairs)

    def combinations(self, n):
        return n * (n - 1) / 2
