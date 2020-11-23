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

    def __len__(self):
        length = 1
        dummy_next = self.next
        while dummy_next:
            length += 1
            dummy_next = dummy_next.next
        return length

    def __eq__(self, other):
        head = self
        while other:
            if other.val == head.val:
                other = other.next
                head = head.next
            else:
                return False
        return True


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    """
    passes 44/61 tests
    """
    counter = 0
    saved_head = None

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if self.counter == 0:
            self.saved_head = head
        if not head:
            return True
        if not root:
            return False
        if root.val == head.val:
            if not head.next:
                return True
            self.counter += 1
            return self.isSubPath(head.next, root.left) or self.isSubPath(head.next, root.right)
        else:
            if not root.right and not root.left:
                return False
            else:
                self.counter += 1
                return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) \
                    or self.isSubPath(self.saved_head, root.left) or self.isSubPath(self.saved_head, root.right)


# class Solution2:
#     def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
#         pass
