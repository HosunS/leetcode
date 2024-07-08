class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        start at the first friend that you started at
        the list is a cycle, so once you hit the nth friend you go back to the first friend that is available

        iterate through until the value of n is 1
        '''
        if n==1: 
            return 1
        elif k==1:
            return n
        elif n>=k:
            next_n = n - n//k
            z = self.findTheWinner(next_n, k) - 1
            x = (z-n%k + next_n) % next_n
            return x + x//(k-1) + 1
        else:
            return (k + self.findTheWinner(n-1, k) -1) % n + 1

