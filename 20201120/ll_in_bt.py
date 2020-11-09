"""
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some
downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head or not root:
            return False
        d_root = root
        d_head = head
        while d_head:
            if d_root.val == d_head.val:
                if d_root.left and d_root.left == d_head.next:
                    d_root = d_root.left
                    d_head = d_head.next
                elif d_root.right and d_root.right == d_head.next:
                    d_root = d_root.right
                    d_head = d_head.next
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    test_list = ListNode(0, ListNode(1, ListNode(2)))
    test_tree = TreeNode(0)
    print(solution.isSubPath(test_list, test_tree))
