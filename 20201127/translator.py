from list_in_tree import *


class ListTranslator:

    def translate(self, array_list: list) -> ListNode:
        linked_list = ListNode(val=None)
        for elem in reversed(array_list):
            linked_list = ListNode(val=elem, next=linked_list)
        return linked_list


# class TreeTranslator:
#
#     def translate(self, tree_list: list) -> TreeNode:
#         if not tree_list:
#             return TreeNode(val=None)
#         tree = TreeNode(tree_list[0])
#         branches = tree_list[1:] if len(tree_list) > 1 else None
#         while branches:
#             if len(branches) > 1:
#                 tree.right = branches[1]
#                 del branches[1]
#             tree.left = branches[0]
#             del branches[0]
#             return self.translate(branches)
#         return tree


if __name__ == "__main__":
    list_t = ListTranslator()
    check_list = ListNode(5, ListNode(3, ListNode(9)))
    print(list_t.translate([5, 3, 9]) == check_list)

    # tree_t = TreeTranslator()
    # check_tree = TreeNode(5, left=TreeNode(3, right=TreeNode(9)), right=TreeNode(4))
    # print(tree_t.translate([5, 3, 4, None, 9]) == check_tree)
