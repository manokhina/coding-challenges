"""
A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that
each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""


class Solution:
    def partitionLabels(self, s: str):
        if s[0] == s[-1]:
            return [len(s)]
        labeled_chars_list = list()
        for item in set(s):
            first, last = s.find(item), s.rfind(item)
            if first != last:
                labeled_chars_list.append(f'{first}S'.zfill(4))
                labeled_chars_list.append(f'{last}E'.zfill(4))
            else:
                labeled_chars_list.append(f'{first}O'.zfill(4))
        chars_indices_sorted = sorted(labeled_chars_list)
        lengths = list()
        c = 0
        prev = -1
        for i in chars_indices_sorted:
            current_num = int(i[:-1])

            if "S" in i:
                c += 1
            if "E" in i:
                c -= 1
            if c == 0:
                cur_length = current_num - prev
                lengths.append(cur_length)
                prev = current_num
        return lengths
