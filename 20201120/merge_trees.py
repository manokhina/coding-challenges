"""
Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of new tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        new_tree = TreeNode(t1.val + t2.val)
        new_tree.left = self.mergeTrees(t1.left, t2.left)
        new_tree.right = self.mergeTrees(t1.right, t2.right)

        return new_tree


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(val=0)
    t2 = TreeNode(val=5)
    print(solution.mergeTrees(t1, t2))
