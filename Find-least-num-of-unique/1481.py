class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int: 
        '''
        going to implement a dictionary that can keep track of the amount of removes
        we need to try to find the most amount of 0's we can create through the use of the removes
        and return the count of non-zero elements in the dictionary
        '''
        numCount = Counter(arr)
        values = list(numCount.values())
        values.sort()
        print(values)
        s = 0
        index = 0
        while s <= k and index < len(arr):
            s += values[index]
            index += 1

        return len(values) - index + 1 if sum(values) > k else 0
            
