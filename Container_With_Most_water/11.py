class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute Force takes too long
        # currMax = 0
        # for i in range(0,len(height)-1):
        #     for j in range(i + 1, len(height)):
        #         width = j - i
        #         highest_height = min(height[i],height[j])
        #         if width * highest_height > currMax:
        #             currMax = width * highest_height
        
        # return currMax

        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currentArea = min(height[left] , height[right]) * (right - left)
            maxArea = max(maxArea,currentArea)

            if height[left] < height[right]: #we find the pointer that points to the lower height we do this until we reach the center
                left+=1
            else:
                right -= 1
            
        return maxArea
