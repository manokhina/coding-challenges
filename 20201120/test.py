import unittest
from merge_trees import *


class TestSolution(unittest.TestCase):
    def test_empty(self):
        solution = Solution()
        test_tree1 = TreeNode()
        test_tree2 = TreeNode()
        control_tree = TreeNode()
        self.assertEqual(solution.mergeTrees(test_tree1, test_tree2), control_tree)

    def test_non_empty(self):
        solution = Solution()
        test_tree1 = TreeNode(5, left=TreeNode(5, left=TreeNode(4)), right=TreeNode(0, left=TreeNode(2)))
        test_tree2 = TreeNode(6, right=TreeNode(4))
        control_tree = TreeNode(11, left=TreeNode(5, left=TreeNode(4)), right=TreeNode(4, left=TreeNode(2)))
        self.assertEqual(solution.mergeTrees(test_tree1, test_tree2), control_tree)


if __name__ == '__main__':
    unittest.main()
