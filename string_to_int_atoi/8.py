class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        need to iterate through each character in the string
        ignore white space
        determine sign by checking the next char is - or +

        '''
        ans = ''

        for char in s:
            if char == ' ' and len(ans) == 0:
                continue
            if char != ' ' and (char in '+-' or char.isnumeric()) and len(ans) == 0: 
                ans += char
            elif char.isnumeric():
                ans += char
            else:
                break
        
        if ans == '' or ans in '+-':
            return 0
        else:
            if int(ans) < -(2 ** 31):
                return -(2**31)
            elif int(ans) > (2 ** 31 - 1):
                return (2 ** 31 - 1)
            else:
                return int(ans)


