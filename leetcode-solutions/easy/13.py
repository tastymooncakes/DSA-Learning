class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = ""
        for i in s:
            result += map[i]
            if prev is not "" and map[prev] < map[i]:
                result -= 2*map[prev]
            prev = i

        return result