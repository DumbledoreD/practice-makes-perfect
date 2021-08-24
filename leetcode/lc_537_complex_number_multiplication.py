class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = self._num_to_tuple(num1)
        num2 = self._num_to_tuple(num2)

        a, b = num1
        c, d = num2

        ac = a * c
        bd = b * d
        ad = a * d
        bc = b * c

        return f"{str(ac - bd)}+{str(ad + bc)}i"

    def _num_to_tuple(self, num):
        real, imaginary = num.split("+")
        return (int(real), int(imaginary.replace("i", "")))
