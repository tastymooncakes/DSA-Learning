class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = None
        for i in nums:
            if closest is None:
                closest = i
            if abs(i) < abs(closest):
                closest = i
            if abs(i) == abs(closest):
                if closest < i:
                    closest = i
        return closest