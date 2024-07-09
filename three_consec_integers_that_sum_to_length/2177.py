class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        '''
        given num we need to return three consecutive integers that sum up to num
        We start at 1 and not 0

        '''
        if num == 0:
            return [-1, 0 , 1]
        for i in range(num//3 - 1 ,num - 1):
            if (i-1) + (i+1) + (i) == num:
                return [i - 1 , i  , i+1]
            elif (i-1) + (i+1) + (i) > num:
                return []
        
        return []
