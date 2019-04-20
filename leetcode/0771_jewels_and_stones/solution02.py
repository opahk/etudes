class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        cache = dict()
        for j in J:
            cache[j] = 1
        for s in S:
            if cache.get(s):
                count += 1
        return count
