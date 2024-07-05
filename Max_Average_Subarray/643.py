class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = 0
        if len(nums) == 1:
            return nums[0]/k
            
        for i in range(len(nums) - k + 1):
            currSum = nums[i]
            for j in range(1, k):
                currSum += nums[i + j]
            currSum = currSum
            if currSum > mx:
                mx = currSum
        return mx/k

        # curr = mx = sum(nums[:k])

        # for i in range(k , len(nums)):
        #     curr += nums[i] - nums[i-k]
        #     mx = max(mx,curr)
        
        # return mx / k
