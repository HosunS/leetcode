class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        first letter will always be the first,
        we need a dictionary that has a list in each key:
        there will be the same amount of keys as there are rows
        and we will iterate through the str until we hit the end and
        we iterate through the dictionaries keys back and forth
        '''
        dict = defaultdict(list)
        for i in range(numRows):
            dict[i]
            
        counter = 0
        reverse = False

        for char in s:
            dict[counter].append(char) 
            if reverse == False:
                counter += 1
            elif reverse == True:
                counter -= 1
            if counter == numRows-1:
                reverse = True
            elif counter == 0:
                reverse = False
        
        ans = ''

        for key in dict:
            curr = dict[key]
            ans += ''.join(curr)

        return ans


    

