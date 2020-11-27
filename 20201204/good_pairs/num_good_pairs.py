"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_pairs = 0
        if len(nums) < 2:
            return num_pairs
        counter = Counter(nums)
        repeated_counter = dict(filter(lambda elem: elem[1] > 1, counter.items()))
        for item, val in repeated_counter.items():
            num_pairs += self.combinations(val, 2)
        return int(num_pairs)

    @staticmethod
    def factorial(n):
        res = 1
        while n > 0:
            res *= n
            n -= 1
        return res

    def combinations(self, n, k):
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

