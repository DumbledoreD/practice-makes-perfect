class Solution:
    def longestPalindrome(self, s: str) -> str:
        self._s = s

        div, mod = divmod(len(s), 2)
        l, r = (div, div) if mod else (div - 1, div)

        longest = ""

        while l >= 0 and r < len(self._s):
            longest_conceivable_length = (l + 1) * 2
            if longest_conceivable_length <= len(longest):
                break

            left_palindrome = self._longest_palindrome_from_i(l)
            right_palindrome = self._longest_palindrome_from_i(r)
            longest = max(longest, left_palindrome, right_palindrome, key=len)

            l -= 1
            r += 1

        return longest

    def _longest_palindrome_from_i(self, i):
        # As center
        l = r = i

        while l >= 0 and r < len(self._s) and self._s[l] == self._s[r]:
            l -= 1
            r += 1

        center_palindrome = self._s[l + 1 : r]

        # As left
        l, r = i, i + 1
        while l >= 0 and r < len(self._s) and self._s[l] == self._s[r]:
            l -= 1
            r += 1

        left_palindrome = self._s[l + 1 : r]

        return (
            left_palindrome
            if len(left_palindrome) > len(center_palindrome)
            else center_palindrome
        )


if __name__ == "__main__":
    print(Solution().longestPalindrome("ac"))
