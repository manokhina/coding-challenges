"""
https://leetcode.com/problems/sort-array-by-parity-ii/

Given an array A of non-negative integers, half of the integers in A are odd,
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""


class Solution:
    def sortArrayByParityII(self, nums):
        for i in range(len(nums)):
            if i % 2 != nums[i] % 2:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParityII([4, 2, 5, 9]))
    print(solution.sortArrayByParityII([4, 2, 5, 7, 5, 8]))


