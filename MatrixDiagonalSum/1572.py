class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        0, 0
        1 ,1
        2 ,2
        2 ,0

        '''
        diagonalSum = 0
        center = mat[len(mat)//2][len(mat)//2]
        # print(center)
        N = len(mat)
        for r in range(N):
            for c in range(N):
                if r == c:
                    # print("if r == c", r , c , mat[r][c])
                    diagonalSum += mat[r][c]
                if r + c == len(mat) - 1:
                    # print("if r + c" , r , c, mat[r][c])
                    diagonalSum += mat[r][c]

        if len(mat) % 2 == 0:
            return diagonalSum
        else:
            return diagonalSum - center
