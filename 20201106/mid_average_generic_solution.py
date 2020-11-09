"""
[10, 20, 1, 5, 6] -> [10, 5, 6] -> 21/5 = 4.2
"""

from self_balancing_binary_search_tree import SBBST


class Solution:
    """
    Assumptions:
    1) We don't have to implement self-balancing tree itself
    as long as we know how to import it and what's the time/space complexity
    of this implementation ¯\_(ツ)_/¯
    2) If k = 0, calculate the average of all the queue
    3) k may be different each time. If it's the same, it's a bit simpler
    """

    def __init__(self):
        self.array = list()
        self.sbt = None

    def generate_tree(self, array, k):
        self.sbt = SBBST(array[-k:])

    @staticmethod
    def get_sum(tree):
        return sum(tree.inOrder())

    def prune_tree(self, tree):
        pruned_tree = tree
        prune_size = int(tree.getSize() / 5)
        for _ in range(prune_size):
            pruned_tree.delete(self.sbt.getMinVal())
            pruned_tree.delete(self.sbt.getMaxVal())
        return pruned_tree

    def get_average(self, val, k):
        self.array.append(val)
        if k == 0:
            return sum(self.array) / len(self.array)
        # self.sbt.insert(val)
        self.generate_tree(self.array, k)
        pruned_tree = self.prune_tree(self.sbt)
        return self.get_sum(pruned_tree) / k


if __name__ == '__main__':
    solution = Solution()
    print(solution.get_average(10, 0))
    print(solution.get_average(20, 0))
    print(solution.get_average(1, 0))
    print(solution.get_average(5, 0))
    print(solution.get_average(6, 5))
