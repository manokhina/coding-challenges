"""
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

"""
import numpy as np
from collections import Counter


class Solution:
    def sortColors(self, nums):
        counter = Counter(nums)
        nums[:] = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]


if __name__ == "__main__":
    solution = Solution()
    for _ in range(50):
        nums = np.random.randint(0, 3, 10).tolist()
        sorted_nums = sorted(nums)
        solution.sortColors(nums)
        assert nums == sorted_nums
