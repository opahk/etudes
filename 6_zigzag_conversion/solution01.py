class Solution:
    def convert(self, s: str, numRows: int) -> str:
        period = 2 * numRows - 2 if numRows > 1 else 1
        output = [list() for r in range(period // 2 + 1)]
        for i, char in enumerate(s):
            row, index = self.index_map(i, period)
            output[row].append(char)
        return "".join(["".join(row) for row in output])

    def index_map(self, i: int, period: int) -> int:
        # first row
        if i % period == 0:
            return 0, i // period

        # last row
        if i % period == period // 2:
            return period // 2, (i // period)

        for j in range(1, period // 2):
            if i % period == j:
                return j, 2 * (i // period)
            if i % period == period - j:
                return j, 1 + 2 * (i // period)
