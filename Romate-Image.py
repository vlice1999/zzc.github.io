class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix[0])
        for i in range(l):
            j=0
            for j in range(i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(l):
            for j in range(l/2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][l-j-1]
                matrix[i][l-j-1]=temp
