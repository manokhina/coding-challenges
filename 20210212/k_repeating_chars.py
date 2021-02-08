"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency
of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Algo:

Find the number of unique characters in the string s and store the count in variable maxUnique.
For s = aabcbacad, the unique characters are a,b,c,d and maxUnique = 4.

Iterate over the string s with the value of currUnique ranging from 1 to maxUnique.
In each iteration, currUnique is the maximum number of unique characters that must be present in the sliding window.

The sliding window starts at index windowStart and ends at index windowEnd and slides over string s until windowEnd
reaches the end of string s. At any given point, we shrink or expand the window to ensure that the number of
unique characters is not greater than currUnique.

If the number of unique character in the sliding window is less than or equal to currUnique, expand the window
from the right by adding a character to the end of the window given by windowEnd

Otherwise, shrink the window from the left by removing a character from the start of the window given by windowStart.

Keep track of the number of unique characters in the current sliding window having at least k frequency given
by countAtLeastK. Update the result if all the characters in the window have at least k frequency.
"""
from collections import Counter


class Solution:
    """30/31 tests passed"""
    def longestSubstring_slow(self, s: str, k: int) -> int:
        if min(Counter(s).values()) >= k:
            return len(s)
        for length in reversed(range(1, len(s))):
            for i in range(len(s) - length + 1):
                counter = Counter(s[i:i+length])
                print(s[i:i+length], length)
                if min(counter.values()) >= k:
                    return length
        return 0

    def longestSubstring(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("aaabb", 3))
    print(solution.longestSubstring("ababbc", 2))
    print(solution.longestSubstring("aaaaaaaaabbbcccccddddd", 5))
