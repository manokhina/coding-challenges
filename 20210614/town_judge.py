"""
https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labelled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""


class Solution:
    def findJudge(self, n, trust) -> int:
        if n == 1: return 1
        who_trusts = list(i[0] for i in trust)
        whom_trust = list(i[1] for i in trust)
        if set(who_trusts) == set(whom_trust) or len(set(who_trusts)) == n:
            return -1
        judge_found = 0
        judge = -1
        for i in range(1, n + 1):
            if i not in who_trusts and whom_trust.count(i) == n - 1:
                judge_found += 1
                judge = i
        return judge if judge_found == 1 else -1


sol = Solution()
print(sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(sol.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

