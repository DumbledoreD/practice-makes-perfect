from collections import Counter


class Solution:
    """
    0: zero     counter["z"]
    1: one                      counter["o"] - count[0,2,4]
    2: two      counter["w"]
    3: three                    counter["h"] - count[8]
    4: four     counter["u"]
    5: five                     counter["f"] - count[4]
    6: six      counter["x"]
    7: seven                    counter["s"] - count[6]
    8: eight    counter["g"]
    9: nine                     counter["i"] - count[5,6,8]
    """

    def originalDigits(self, s: str) -> str:
        count = [0] * 10
        char_counter = Counter(s)

        count[0] = char_counter["z"]
        count[2] = char_counter["w"]
        count[4] = char_counter["u"]
        count[6] = char_counter["x"]
        count[8] = char_counter["g"]

        count[1] = char_counter["o"] - count[0] - count[2] - count[4]
        count[3] = char_counter["h"] - count[8]
        count[5] = char_counter["f"] - count[4]
        count[7] = char_counter["s"] - count[6]
        count[9] = char_counter["i"] - count[5] - count[6] - count[8]

        return "".join(str(i) * c for i, c in enumerate(count))
