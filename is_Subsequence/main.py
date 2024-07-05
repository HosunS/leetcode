class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s is a subsequence
        if len(s) > len(t):
            return False
        curr = 0
        for i in range(len(s)):
            for j in range(curr,len(t)):
                curr += 1
                if s[i] == t[j]:
                    break
                if j == len(t) -1 and s[i] != t[j]:
                    return False
            if curr == len(t) and i < len(s) - 1:
                return False
        
        return True
                
