import math

class Solution:
    def reverse(self, x: int, order: int = None) -> int:
        if x == 0:
            return x
        positive_int = x if x > 0 else -x
        if not order:
            order = int(math.log(positive_int, 10))
        if order == 0:
            return x
        reversed_int = self.reverse(positive_int % 10**order, order - 1) * 10 + positive_int // 10**order
        signed_reversed_int = reversed_int if x > 0 else -reversed_int
        if signed_reversed_int > 2147483646 or signed_reversed_int < -2147483647:
            return 0
        return signed_reversed_int
