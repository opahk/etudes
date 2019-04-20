class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        positive_int = x if x > 0 else -x
        string = str(positive_int)
        reverse_string = ""
        for char in string:
            reverse_string = "".join([char,reverse_string])
        reverse_int = int(reverse_string)
        signed_reverse_int = reverse_int if x > 0 else -reverse_int
        if signed_reverse_int > 2147483646 or signed_reverse_int < -2147483647:
            return 0
        return signed_reverse_int import math

