class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            for j in J:
                if s == j:
                    count += 1
                    break
        return count

