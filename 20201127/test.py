import unittest
from list_in_tree import *
from translator import *


class TestSolution(unittest.TestCase):

    def test_both_empty(self):
        solution = Solution()
        control_tree = TreeNode()
        control_list = ListNode()
        control_solution = solution.isSubPath(control_list, control_tree)
        self.assertTrue(control_solution)

    def test_tree_empty(self):
        solution = Solution()
        lt = ListTranslator()
        control_tree = TreeNode()
        control_list = lt.translate([5, 3, 9])  # ListNode(5, ListNode(3, ListNode(9)))
        control_solution = solution.isSubPath(control_list, control_tree)
        self.assertFalse(control_solution)

    def test_non_empty_false(self):
        solution = Solution()
        lt = ListTranslator()
        control_tree = TreeNode(11, left=TreeNode(5, left=TreeNode(4)), right=TreeNode(4, left=TreeNode(2)))
        control_list = lt.translate([5, 3, 9])  # ListNode(5, ListNode(3, ListNode(9)))
        control_solution = solution.isSubPath(control_list, control_tree)
        self.assertFalse(control_solution)

    def test_non_empty_true(self):
        solution = Solution()
        lt = ListTranslator()
        control_tree = TreeNode(11, left=TreeNode(5, left=TreeNode(4)), right=TreeNode(4, left=TreeNode(2)))
        control_list = lt.translate([5, 4])  # ListNode(5, ListNode(4))
        control_solution = solution.isSubPath(control_list, control_tree)
        self.assertTrue(control_solution)
