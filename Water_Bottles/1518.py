class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += (numBottles//numExchange)
            rem = numBottles%numExchange
            numBottles = numBottles //numExchange
            numBottles += rem
        
        return ans
