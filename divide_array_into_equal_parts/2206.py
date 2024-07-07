class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        '''
        input : nums = 2 * n integers
        output : boolean for if len(nums) // 2

        dictionary : holding the occurence of each element in the array
        counter = to the count the pairs
        iterate through the dictionary
            increment the counter for every floor division of occurence by 2
        
        return  len(nums) / 2 and counter
        '''

        pairCounter = 0
        occurenceDict = {}

        for num in nums:
            occurenceDict[num] = occurenceDict.get(num,0) + 1
        
        for occurence in occurenceDict:
            pairCounter += occurenceDict[occurence] // 2
    
        return len(nums) / 2  == pairCounter      
          
