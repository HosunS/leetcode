class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        ans = ''
        for i in range(len(x)-1 , -1, -1):
            if x[i] == '-':
                ans = '-' + ans
            else:
                ans = ans + x[i]
        ans = int(ans) 

        if (ans <= 2 ** 31 -1) and (ans >= -2 ** 31):
            return ans
        else:
            return 0
