class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_length = max(len(num1), len(num2)) + 1
        digits = [None] * max_length

        carry = 0

        for i in range(1, max_length):
            num1_i = len(num1) - i
            num2_i = len(num2) - i

            num1_digit = int(num1[num1_i]) if num1_i >= 0 else 0
            num2_digit = int(num2[num2_i]) if num2_i >= 0 else 0

            carry, digit = divmod(num1_digit + num2_digit + carry, 10)
            digits[max_length - i] = str(digit)

        digits[0] = "1" if carry else ""

        return "".join(digits)
