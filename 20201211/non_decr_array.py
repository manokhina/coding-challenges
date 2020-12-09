"""
Given an array nums with n integers, your task is to check if it could become 
non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True
        dif = [i - j for i, j in zip(nums[1:], nums[:-1])]
        negatives = [d < 0 for d in dif]
        num_negatives = sum(negatives)
        if num_negatives > 1:
            return False
        if num_negatives == 1 and negatives.index(True) not in {0, length-2}:
            neg_idx = negatives.index(True)
            if abs(dif[neg_idx]) > max(dif[neg_idx + 1], dif[neg_idx - 1]):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility([4, 2, 3]))
    print(solution.checkPossibility([3, 4, 2, 3]))
    print(solution.checkPossibility([1,3,2]))
    print(solution.checkPossibility([1,3,5,2,4])) #[2,2,-3,2]
    print(solution.checkPossibility([-1,4,2,3]))
