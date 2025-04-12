class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = min(len(word1), len(word2))
        merged = ""

        for i in range(shortest):
            merged += word1[i] + word2[i]

        merged += word1[shortest:]
        merged += word2[shortest:]

        return merged