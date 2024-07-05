# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls 
# if they are put in his new invented basket. Rick has n empty baskets, 
# the ith basket is at position[i], Morty has m balls and needs to distribute the
# balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        ans = 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.canWePlace(position, mid, m):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans

    def canWePlace(self, arr, dist, balls):
        countBalls = 1
        lastPlaced = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
            if countBalls >= balls:
                return True
        return False