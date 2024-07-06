class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height) -1
        res = 0

        while l < r:
            area = (r - l) *  min(height[r], height[l])

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            res = max(res,area)

        return res
