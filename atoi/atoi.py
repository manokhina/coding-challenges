class Solution:
    max_int = 2147483647
    min_int = -2147483648

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if not s:
            return 0
        if not s[0].isdigit() and s[0] not in "+-":
            return 0
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            sign = -1
        result = ""
        for char in s:
            if char.isdigit():
                result += char
            else:
                if result:
                    interim = int(result) * sign if result else 0
                    return max(min(interim, self.max_int), self.min_int)
                else:
                    return 0
        interim = int(result) * sign if result else 0
        return max(min(interim, self.max_int), self.min_int)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("74859jfth"))
    print(solution.myAtoi("  -74"))
    print(solution.myAtoi("+876"))
