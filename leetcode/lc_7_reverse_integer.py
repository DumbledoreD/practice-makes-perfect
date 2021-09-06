class Solution:
    _MAX = str(2 ** 31 - 1)

    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        reversed_x = str(abs(x))[::-1]

        if abs(x) > 10 ** 9 and not self._validate(reversed_x, sign):
            return 0

        return sign * int(reversed_x)

    def _validate(self, str_int, sign):
        for i in range(len(str_int)):
            digit = int(str_int[i])

            max_digit_index = len(self._MAX) - len(str_int) + i
            max_digit_offset = 1 if sign == -1 and i == -1 else 0
            max_digit = int(self._MAX[max_digit_index]) + max_digit_offset

            if digit < max_digit:
                return True

            if digit > max_digit:
                return False

        return True
