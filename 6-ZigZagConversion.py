class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s_list = ["" for i in range(numRows)]
        step = -1
        pos = 0
        for value in s:
            s_list[pos] += value
            if pos == numRows - 1 or pos == 0:
                step *= -1
            pos += step
        return "".join(s_list)