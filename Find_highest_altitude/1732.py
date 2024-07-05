class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        pre = 0
        for i in gain:
            pre += i
            if pre > mx:
                mx = pre
        return mx
